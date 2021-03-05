import logging

class KEG_Log():
    def __init__( self, level=1, file_name='KEG_Log.log' ):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel( level )# 1 

        self.sh = logging.StreamHandler()
        self.logger.addHandler( self.sh )
        
        self.fh = logging.FileHandler( file_name )
        self.logger.addHandler( self.fh )
        
        # ログの出力形式の設定
        self.formatter = logging.Formatter( '%(asctime)s:%(filename)s:[%(levelname)s]%(message)s' )
        self.fh.setFormatter( self.formatter )
        self.sh.setFormatter( self.formatter )

    def info( self, text ):
        self.logger.info( text )
    
    def warning( self, text ):
        self.logger.warning( text )
    
    def error( self, text ):
        self.logger.error( text )

    def critical( self, text ):
        self.logger.critical( text )
    
    def debug( self, text ):
        self.logger.debug( text )

#KEG_Log().info( "TEST" )
#log = KEG_Log()
#log.critical( "TEST" )

"""
DEBUG:10
INFO:20
WARNING:30
ERROR:40
CRITICAL:50
"""
