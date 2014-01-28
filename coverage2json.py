import sys
import json
from cPickle import load

sys.stdout.write(json.dumps(load(sys.stdin)))
