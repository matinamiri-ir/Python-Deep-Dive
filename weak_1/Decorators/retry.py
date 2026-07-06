import time
from random import uniform
from typing import Type, Tuple, Callable, Any
from functools import wraps
class DbError(Exception):
    pass


class DelayError(Exception):
    pass


class DisconnectError(Exception):
    pass

class StopTry(Exception):
    pass 

class WifiDisconnected(Exception):
    pass


def retry(
          max_retry:int = 3,
          base_delay:int = 1,
          expo:int = 2,
          exceptions:Tuple[Type[Exception],...]=(Exception,)):
    '''
    decorate an API handler and retry requests if dont get response
    '''
    
    def decorator(func:Callable)->Callable:
        @wraps(func)
        def wrapper(*args:Any,**kwargs:Any):
            for test in range(1, max_retry + 1):
                try:
                    data = func(*args, **kwargs)
                    print(f'got result in {test+1}`th try')
                    print(f'{data=}')
                    return data
                except exceptions :
                        expo_delay = base_delay * (expo ** (test - 1)) 
                        delay = uniform(expo_delay * 0.8, expo_delay * 1.2)
                        print(f'{delay=:.2f}s',"*"*50,sep='\n')
                        time.sleep(delay)
                        if test == max_retry:
                            raise
                
        return wrapper
    return decorator


@retry(max_retry=3, exceptions=(DbError,DelayError,DisconnectError))
def test_api():
    delay = uniform(0,1)
    time.sleep(delay)
    
    match delay:
        case _ if 0.1 < delay < 0.2:
            return f'{delay:.3f}'
        case _ if 0.2 < delay < 0.4:
            raise DbError('can`t fetch data, please try again...')
        case _ if delay < 0.1:
            raise WifiDisconnected('oh, your WIFI disconnected.')
        case _ if 0.5 < delay < 0.8:
            raise DelayError('database have delay, please wait...')
        case _ if 0.8 < delay < 1 :
            raise DisconnectError('we lost our connection to database, sorry')



if __name__ =='__main__':
    test_api()
