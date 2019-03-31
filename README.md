# picoCTF-FlaskSkeletonKey-SessionEdit
How I got the correct session id for to solve flask skeleton key in the picoCTF 2018 hackathon.

The problem can be found here : http://2018shell2.picoctf.com:53999

After using SSTI to find the secret key, I decoded the sessionID using BurpSuite to intercept the request. After decoding, I just change the user-id to 1 so the webpage would think I was the admin, and re-encoded the information with the secret-key.

This is just the code that found that correct sessionID.
