from pynput.keyboard import Key, Controller
import time
import sys
import argparse
import random

def parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=r'''
                        .="=.                .="=.
                      _/.-.-.\_     _      _/.-.-.\_     _
                     ( ( o o ) )    ))    ( ( o o ) )    ))
                      |/  "  \|    //      |/  "  \|    //
      .-------.        \'---'/    //        \'---'/    //
     _|~~ ~~  |_       /`"""`\\  ((         /`"""`\\  ((
   =(_|_______|_)=    / /_,_\ \\  \\       / /_,_\ \\  \\
     |:::::::::|      \_\\_'__/ \  ))      \_\\_'__/ \  ))
     |:::::::[]|       /`  /`~\  |//        /`  /`~\  |//
     |o=======.|      /   /    \  /        /   /    \  /
     `"""""""""`  ,--`,--'\/\    /     ,--`,--'\/\    /
                   '-- "--'  '--'       '-- "--'  '--' '''
    )
    parser.add_argument('-t','--time',dest='time', default=5, help="Seconds to Wait until start typing")
    parser.add_argument('-H', '--human', dest='human', action="store_true", help="Slows down the output to 1 char per 300ms")

    parser.add_argument(dest='cmd', choices={'string','file'}, help="do you want to output a string, or read a file")
    parser.add_argument(dest='payload', help="String or Filepath")

    return parser.parse_args()

def main():
    args = parse_args()

    sleep_time = args.time    
    while args.time > 0:
        print("Waiting %is until typing begins, stop with Ctrl+c" % (args.time), end='\r')
        args.time -= 1
        time.sleep(1)

    keyboard = Controller()

    if args.cmd == 'string':
        payload = args.payload
    elif args.cmd == 'file':
        try:
            with open(args.payload) as fh:
                payload = fh.read()
        except OSError as err:
            print("[EE]: Could not read file: %s" % (err))
            sys.exit(1)

    if args.human:
        for i in payload:
            keyboard.type(i)
            time.sleep(random.randrange(200,400)/1000)
    else:
        keyboard.type(payload)
if __name__ == '__main__':
    main()
