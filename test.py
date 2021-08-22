import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='uft-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='uft-8')

print('-'*30)
