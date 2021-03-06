import numpy as np
import time as tm
import idtxl.estimators_fast_pid as epid

def test_pid_xor_imposed():
    """Test PID estimator on logical XOR with imposed probabilities."""
    alph_x = 2
    alph_y = 2
    alph_z = 2

    x = np.array([0, 0, 1, 1])
    y = np.array([1, 0, 1, 0])
    z = np.logical_xor(x, y).astype(int)

    cfg = {
        'alph_s1': alph_x,
        'alph_s2': alph_y,
        'alph_t': alph_z,
        'max_unsuc_swaps_row_parm': 3,
        'num_reps': 63,
        'max_iters': 10000
    }

    tic = tm.time()
    est = epid.pid(x, y, z, cfg)
    toc = tm.time()

    print('\nPID evaluation       {:.3f} seconds\n'.format(toc - tic))
    print('Uni s1              ', est ['unq_s1'])
    print('Uni s2              ', est ['unq_s2'])
    print('Shared s1_s2        ', est ['shd_s1_s2'])
    print('Synergy s1_s2       ', est ['syn_s1_s2'])


if __name__ == '__main__':
    test_pid_xor_imposed()
