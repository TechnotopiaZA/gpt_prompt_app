from flask import render_template, request, redirect, url_for, flash
from . import db
from .forms import PromptForm, SettingsForm
from .models import Prompt

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/settings', methods=['GET', 'POST'])
    def settings():
        form = SettingsForm()
        if form.validate_on_submit():
            flash('Settings updated successfully!', 'success')
            return redirect(url_for('index'))
        return render_template('settings.html', form=form)

    @app.route('/create_prompt', methods=['GET', 'POST'])
    def create_prompt():
        form = PromptForm()
        if form.validate_on_submit():
            new_prompt = Prompt(
                role=form.role.data,
                needs=form.needs.data,
                task=form.task.data,
                details=form.details.data,
                format=form.format.data
            )
            db.session.add(new_prompt)
            db.session.commit()
            flash('Prompt created successfully!', 'success')
            return redirect(url_for('prompts'))
        return render_template('create_prompt.html', form=form)

    @app.route('/edit_prompt/<int:prompt_id>', methods=['GET', 'POST'])
    def edit_prompt(prompt_id):
        prompt = Prompt.query.get_or_404(prompt_id)
        form = PromptForm()
        if form.validate_on_submit():
            prompt.role = form.role.data
            prompt.needs = form.needs.data
            prompt.task = form.task.data
            prompt.details = form.details.data
            prompt.format = form.format.data
            db.session.commit()
            flash('Prompt updated successfully!', 'success')
            return redirect(url_for('prompts'))
        elif request.method == 'GET':
            form.role.data = prompt.role
            form.needs.data = prompt.needs
            form.task.data = prompt.task
            form.details.data = prompt.details
            form.format.data = prompt.format
        return render_template('edit_prompt.html', form=form)

    @app.route('/delete_prompt/<int:prompt_id>', methods=['POST'])
    def delete_prompt(prompt_id):
        prompt = Prompt.query.get_or_404(prompt_id)
        db.session.delete(prompt)
        db.session.commit()
        flash('Prompt deleted successfully!', 'success')
        return redirect(url_for('prompts'))

    @app.route('/prompts')
    def prompts():
        all_prompts = Prompt.query.all()
        return render_template('prompts.html', prompts=all_prompts)

    @app.route('/help')
    def help():
        return render_template('help.html')
