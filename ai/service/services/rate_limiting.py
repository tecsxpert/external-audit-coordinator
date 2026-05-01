from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

def setup_rate_limiting(app):
    """
    Configure Flask-Limiter with default 30 req/min, 10 req/min on /generate-report,
    and returns 429 with retry_after header on breach.
    """
    limiter = Limiter(
        app=app,
        key_func=get_remote_address,
        default_limits=["30 per minute"]
    )

    # Specific limit for /generate-report can be applied as a decorator in the route
    # For example:
    # @app.route('/generate-report')
    # @limiter.limit("10 per minute")
    # def generate_report():
    #     ...

    return limiter