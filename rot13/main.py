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
import cgi

form = """
<h2>Enter some text to ROT13:</h2>
<form method="post">
    <textarea rows="7" cols="50" name="text">%(text)s</textarea>
    <br>
    <input type="submit">
</form>
"""
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
         'r','s','t','u','v','w','x','y','z']

def text_entered(s):
    x = list(str(s))
    y = []
    for i in range(len(s)):
        if x[i].isupper():
            y.append(i)

    s = s.lower()
    s = list(str(s))
    a = []
    for i in range(len(s)):
        if s[i] in alpha:
            if alpha.index(s[i])<=12:
                b = alpha.index(s[i])+13
                a.append(alpha[b])
            else:
                b = alpha.index(s[i])-13
                a.append(alpha[b])
                # a.append(s[i])
        else:
            a.append(s[i])

    for i in y:
        a[i] = a[i].upper()

    c = ''.join(a)
    return c

def escape_HTML(s):
    return cgi.escape(s, quote=True)

class MainPage(webapp2.RequestHandler):
    def write_out(self,text=""):
        self.response.out.write(form % {"text": escape_HTML(text)})

    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.write_out()

    def post(self):
        text = self.request.get('text')
        # self.response.out.write(text)
        # self.response.out.write(text_entered(text))
        if text:
            self.write_out(text_entered(text))

app = webapp2.WSGIApplication([('/',MainPage)],debug=True)
