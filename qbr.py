from sys import exit as Die
try:
    import sys
    import argparse
    from video import webcam
    from combiner import combine
except ImportError as err:
    Die(err)

class Qbr:
    def run(self):
        state         = webcam.scan()
        if not state:
            print('\033[0;33m[QBR SCAN ERROR] Ops, you did not scan in all 6 sides.')
            print('Please try again.\033[0m')
            Die(1)

        unsolvedState = combine.sides(state)
        print(unsolvedState)

        Die(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    Qbr( ).run()
