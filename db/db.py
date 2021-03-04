# coding: utf-8
import sqlite3

class DBConnect:
    def __init__( self ):
        self.connect()

    def connect( self ):
        self.con = sqlite3.connect( 'db/dairy.sqlite3' )
        self.cur = self.con.cursor()

    def end( self ):
        self.con.commit()
        self.con.close()

    def get( self, closed ):
        result = []

        if closed == "all":
            return self.get_all()

        self.cur.execute( "select * from dairy where closed = '" + closed + "'" )
        rows = self.cur.fetchall()
        for row in rows:
            result.append( row )
            #print( row )

        return result
    
    def get_all( self ):
        result = []

        self.cur.execute( "select * from dairy" )
        rows = self.cur.fetchall()
        for row in rows:
            result.append( row )
            #print( row )
        return result    

    def get_select( self, number, mode, item ):
        result = []

        if mode == "all":
            self.cur.execute( "select " + item + " from dairy where number = '" + number + "'" )
        else:
            self.cur.execute( "select " + item + " from dairy where number = '" + number + "' and closed = '" + mode + "'" )
            
        rows = self.cur.fetchall()
        for row in rows:
            result.append( row )
            #print( row )

        return result


    def add( self, data ):
        self.connect()

        if not self.duplicate_sarch( data ):
            self.cur.execute( "insert into dairy( addtime, number, symbol, ls, lots, open_time, close_time, open_price, close_price, profit, images, closed ) \
                               values( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )", data )
        else:
            print( "重複" )

        self.end()
    
    def duplicate_sarch( self, data ):
        self.cur.execute( "select number, closed from dairy where number = '" + data[1] + "' and closed = '" + data[11] + "'" )
        if len( self.cur.fetchall() ):
            return True
        else:
            return False

    def update( self ):
        pass

    def create( self ):
        self.cur.execute( "create table details( \
                            id integer primary key,\
                            number integer, \
                            comment1 string, \
                            comment2 string, \
                            comment3 string, \
                            emotions string, \
                            rules string, \
                            prosess string )" )

        self.cur.execute( 'create table dairy( \
                            id integer primary key,\
                            addtime datetime,\
                            number integer, \
                            symbol string, \
                            ls string,\
                            lots real,\
                            open_time datetime,\
                            close_time datetime,\
                            open_price real,\
                            close_price real,\
                            profit integer,\
                            images string,\
                            closed string )' )

    def join( self ):
        result = []

        self.cur.execute( "select * from dairy left outer join details on dairy.number = details.number" )
        rows = self.cur.fetchall()
        for row in rows:
            result.append( row )
            print( row )
        #print( result )
        return result
        
#db=DBConnect()
#db.join()
#db.create()
#db.add()
#db.get_all()
#db.com_get()
#db.get_select("91655040","all","profit")