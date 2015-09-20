import os

import compress


def move_to_bak(f):
    os.rename(f, 'bak/{0}'.format(f))


def main():
    extensions = ['.table.npy', '.syn1neg.npy', '.syn1.npy', '.syn0.npy']
    for f in os.listdir('.'):
        gzipped_files = map(lambda x: '{0}{1}.gz'.format(f, x), extensions)
        is_gzipped_model = all(map(os.path.isfile, gzipped_files))

        if not is_gzipped_model:
            continue

        compress.compress(f)
        os.remove(f)

        move_to_bak('{0}.gz'.format(f))
        for ff in gzipped_files:
            move_to_bak(ff)

if __name__ == '__main__':
    main()
