from django.utils.deprecation import MiddlewareMixin

from .anonymous_user_data.anonymous_user_with_settings import AnonymousUserWithSettings

class AnonymousUserMiddleware(MiddlewareMixin):
    '''
    Middleware adding settings for the sidebar to anonymous users.

    The middleware first checks if the user is anonymous,
    and if so, creates an instance with sidebar settings for them.
    '''

    def __init__(self, get_response):
        '''
        Class constructor, called when creating an instance.

        The constructor accepts the get_response parameter,
        which is used to capture and process the HTTP request
        within the middleware chain.

        The constructor creates an attribute for this request
        to be available for further request and response processing within the middleware.
        '''
        self.get_response = get_response

    def __call__(self, request):
        '''
        Method allowing the object to be called as a function.

        This method serves as the main entry point for processing an HTTP request.

        First, the method checks if the user is logged in.
        If not, it creates an instance of the AnonymousUserWithSettings class,
        which represents an anonymous user with additional settings.
        This instance is then stored in the request.user attribute.

        If the user is logged in, the request.user attribute remains unchanged.

        Then, the self.get_response(request) function is called,
        which passes the current request to the next middleware in the chain
        and returns the response.
        '''

        if not request.user.is_authenticated:
            request.user = AnonymousUserWithSettings(request)
        else:
            request.user = request.user

        response = self.get_response(request)
        return response
