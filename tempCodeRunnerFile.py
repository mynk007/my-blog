    name=request.form.get('name')
        email=request.form.get('email')
        subject=request.form.get('subject')
        message=request.form.get('message')
        msg=f'Subject: {subject}\n\nName:{name}\n\nEmail: {email}\n\nMessage: {message}'
        sendEmail(msg)
        # flash(u'Invalid password provided', 'error')
        return render_template("index.html",params=params)
