from flask import Flask, redirect,session,flash,url_for,Blueprint,request

logout=Blueprint(
    'logout',__name__,
)

@logout.route('/logout',methods=['GET'])
def logoutuser():
    session.pop('userid',None)
    session.pop('username',None)
    session.pop('email',None)
    return redirect(request.referrer)
    