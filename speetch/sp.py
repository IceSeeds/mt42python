
import speech_recognition as sr
 
class Recording():
    def __init__( self ):
        self.result = ""
    
    def record( self ):
        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print( "何かお話しして下さい。終了する時は「終わりだよ」と。" )
                r.adjust_for_ambient_noise( source )
                audio = r.listen( source )
            try:
                # Google Web Speech APIで音声認識
                text = r.recognize_google( audio, language="ja-JP" )
            except sr.UnknownValueError:
                print( "Google Web Speech APIは音声を認識できませんでした。" )
            except sr.RequestError as e:
                print( "GoogleWeb Speech APIに音声認識を要求できませんでした;"" {0}".format( e ) )
            else:
                if text == "終わりだよ":
                    break
                if text == "改行":
                    self.result += "\n"
                    #print( "改行" )
                print( text )
                self.result += text

        print( "完了。")
        self.view()

    def view( self ):
        print( self.result )
        with open( "recoding.txt", mode="w", encoding="utf-8" ) as file:
            file.write( self.result )

Recording().record()
