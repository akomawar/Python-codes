# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import webapp2
import re

form = """
<form method="post">
    <p><font size='5'><b>Signup</b></font></p>
    <table>
        <tr>
            <td>Username :</td>
            <td><input type="text" name="username" placeholder="Enter Username" value="%(username)s"></td>
            <td style="color:red">%(u_error)s</td>
        </tr>
        <tr>
            <td>Password :</td>
            <td><input type="password" name="password" placeholder="Enter Password"></td>
            <td style="color:red">%(pass_error)s</td>
        </tr>
        <tr>
            <td>Verify Password :</td>
            <td><input type="password" name="vpassword" placeholder="Enter Password Again"></td>
            <td style="color:red">%(ver_error)s</td>
        </tr>
        <tr>
            <td>Email(Optional) :</td>
            <td><input type="text" name="email" placeholder="Enter Email" value=%(email)s></td>
            <td style="color:red">%(email_error)s</td>
        </tr>
    </table>
    <input type="submit">
</form>
"""
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def verify_username(username):
    if USER_RE.match(username)==None:
        return "That's not a valid username."
    else:
        return ""

def verify_password(password):
    if PASS_RE.match(password)==None:
        return "That wasn't a valid password."
    else:
        return ""

def verify_vpassword(password,vpassword):
    if password!=vpassword:
        return "Your passwords didn't match."
    else:
        return ""
def verify_email(email):
    if EMAIL_RE.match(email)==None:
        return "That's not a valid email."
    else:
        return ""

global_username = ""

class MainPage(webapp2.RequestHandler):

    def write_out(self,username="",u_error="",pass_error="",ver_error="",email="",email_error=""):
        self.response.out.write(form % {"username":username,"u_error": u_error,"pass_error":pass_error,"ver_error":ver_error,"email":email,"email_error":email_error})

    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'
        self.write_out()

    def post(self):
        username = self.request.get('username')
        global global_username
        global_username = username
        password = self.request.get('password')
        vpassword = self.request.get('vpassword')
        email = self.request.get('email')

        ver_username = verify_username(username)
        ver_password = verify_password(password)
        ver_vpassword = verify_vpassword(password,vpassword)
        ver_email = verify_email(email)

        if email:
            if ver_username=="" and ver_password=="" and ver_vpassword=="" and ver_email=="":
                self.redirect("/welcome?username=" + username)
            else:
                self.write_out(username,ver_username,ver_password,ver_vpassword,email,ver_email)
        else:
            if ver_username=="" and ver_password=="" and ver_vpassword=="":
                self.redirect("/welcome?username=" + username)
            else:
                self.write_out(username,ver_username,ver_password,ver_vpassword)

class WelcomeHandler(MainPage):
    def get(self):
        # global global_username
        # self.response.out.write(global_username)
        if verify_username(global_username)=="":
            self.response.out.write("<font size='5'><strong>Welcome, "+ global_username +"!</strong></font>")
        else:
            self.response.out.write("/")

app = webapp2.WSGIApplication([('/signup',MainPage),('/welcome',WelcomeHandler)],debug=True)
