# picoCTF-FlaskSkeletonKey-SessionEdit
How I got the correct session id for to solve flask skeleton key in the picoCTF 2018 hackathon.

The problem can be found here : http://2018shell2.picoctf.com:53999
The problem involves breaking into the admin page after logging in.

After obtaining the sessionID (using BurpSuite to intercept the request) it was decoded using the secret key. The secret key was found on the primary upload page using SSTI (Server Side Template Injection) Experimenting a little bit, one finds that the user-id is consecutive. It would then follow that the first user is the admin. So I just changed the user-id to 1 so the webpage would think I was the admin, and re-encoded the information with the secret-key.

This is just the code that was used to generate the correct sessionID.
