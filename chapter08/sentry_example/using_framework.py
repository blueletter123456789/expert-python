import sentry_sdk
from sentry_sdk.integrations.wsgi import SentryWsgiMiddleware


sentry_sdk.init(
    dsn="https://<key>:<secret>@app.getsentry.com/project"
)

application = "something wsgi application"

application = SentryWsgiMiddleware(application)
