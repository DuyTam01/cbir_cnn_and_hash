# các view function của blueprint main
from website.main import bp
from flask import render_template, url_for, flash, redirect
from flask_login import login_required, current_user
from website.main.forms import PostForm
from website.models import Post
from website import db
@bp.route('/')
@login_required
def index():
    return render_template('main/index.html')
@bp.route('/explore')
def explore():
    return render_template('main/index.html')
@bp.route('/upload_post', methods=['POST', 'GET'])
@login_required
def upload_post():
    form = PostForm()
    if form.validate_on_submit():
        p = Post(title=form.title.data,\
                 image_url=form.image_url.data,\
                 categorical=form.categorical.data,\
                 author=current_user)
        db.session.add(p)
        db.session.commit()
        flash('uploaded')
        return redirect(url_for('main.index'))
    return render_template('main/upload_post.html', form=form)