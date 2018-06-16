# Interview Practice

## Questions

**What is the most influential book or blog post you’ve read regarding web
development?**

Clean code by Bob Martin has had the most influence on my code style.  Otherwise
it would be a [talk given by Maile Ohye in 2016](https://wordpress.tv/2016/12/11/maile-ohye-a-view-from-google-the-latest-in-google-and-google/) on the importance of making web
pages light weight. It's safe to say that my focus the last couple of years has
been to write clean simple code and to keep page loads as lean as possible.

**Tell me about a web application you have built. Why did you choose to build it?
What did you learn? What challenges did you face and how did you overcome them?**

I chose to build the [wine journal](https://ourwinejournal.com) project because
I'm interested in small scale, private social networking.  So the goal was to
build an app where friends and family could share information about wine.

I had a couple of big goals when I began the project.  The first was to learn how
to use Flask blueprints to organize an application.  The second was to
expirement with image upload and manipulation.  Incorporating these into the app
were probably my 2 greatest challenges.

Implementing these features required a lot of independent learning and
expirementation.  I literally spent 2 months learning how to use Flask blueprints
and experimenting with various blueprint configurations.  I didn't just want to
build an app, I wanted to build it the way a seasoned professional would build it.

I had to teach myself image upload, manipulation, and storage on Amazon S3 from
scratch. In the course of reading documentation and experimentation I learned
how to upload, resize, rotate, crop, compress and store images on S3.  The allows
the users of the app to upload photos from their phones and makes the sharing
experience more visual.

**Write a function in Python that takes a list of strings and returns a single
string that is an HTML unordered list of those strings.
You should include a brief explanation of your code. Then, what would you have
to consider if the original list was provided by user input?**

See problem1.py.  If this were user generated content then you would need to
sanitize the input data, using something like the Python library "bleach".

**List 2-3 attacks that web applications are vulnerable to. How do these attacks
work? How can we prevent those attacks?**

**XXS - Cross Site Scripting** This form of attack allows a maliscious user to
use a form to add script to the database that will then be printed to the page.
That script may perform some nefarious act when others visit that page.

The solution to this is to sanitize all data before saving it to the database.

**CSRF - Cross Site Request Forgery** This form of attack attempts to hijack
open sessions in the browser.  It attempts to capture session data stored in
the browser and then gain access to the open session.  Once it has access to
the session it can perform any of the actions allowed by the session.

The solution to this is to use a COORs plugin to check the origin of the request
and to deny requests that don't have the same origin as the original session
holder. This is done by creating a secret token that is required along with all
requests but is hidden from the browser.

**Here is some starter code for a Flask Web Application. Expand on that and
include a route that simulates rolling two dice and returns the result in JSON.
You should include a brief explanation of your code.**

**If you were to start your full-stack developer position today, what would be
your goals a year from now?**

My goals would be to have mastered the company's systems (coding standards,
testing, communication, software) and to exceed the expectations of both
supervisors and co-workers.
