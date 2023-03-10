import sentry_sdk


sentry_sdk.init(
    dsn="https://<key>:<secret>@app.getsentry.com/project"
)

try:
    1 / 0
except Exception as ex:
    sentry_sdk.capture_exception(ex)
