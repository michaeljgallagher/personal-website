from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import ContactForm
from flask_mail import Message, Mail
from app import app, db, mail
from models import Project


@app.route("/projects/")
def projects():
    projects = Project.query.all()
    return render_template("projects.html", title="Projects", projects=projects)


@app.route("/project/<int:project_id>")
def project(project_id):
    project = Project.query.get(project_id)
    if not project:
        return render_template("404.html", title="Not Found"), 404
    return render_template("project.html", title=project.name, project=project)


@app.route("/contact/", methods=["GET", "POST"])
def contact():
    form = ContactForm(request.form)
    if request.method == "POST":
        name = request.form.get("name", False)
        email = request.form.get("email", False)
        subject = request.form.get("subject", False)
        message = request.form.get("message", False)
        if form.validate_on_submit():
            msg = Message(
                form.subject.data, sender=email, recipients=["mgallag@protonmail.ch"]
            )
            msg.body = f"{form.name.data} <{form.email.data}>\n\n{form.message.data}"
            mail.send(msg)
            flash(f"Thank you for your message. I'll get back to you soon", "success")
            return redirect(url_for("contact"))
        return render_template("contact.html", title="Contact Me", form=form)

    elif request.method == "GET":
        return render_template("contact.html", title="Contact Me", form=form)
