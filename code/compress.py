import os
import gzip


def decompress(filename):
    in_stream = gzip.GzipFile('{0}.gz'.format(filename), 'rb')
    tmp = in_stream.read()
    in_stream.close()

    out_stream = file(filename, 'wb')
    out_stream.write(tmp)
    out_stream.close()


def compress(filename):
    in_stream = file(filename, 'rb')
    tmp = in_stream.read()
    in_stream.close()

    out_stream = gzip.GzipFile('{0}.gz'.format(filename), 'wb')
    out_stream.write(tmp)
    out_stream.close()


def main():
    for f in os.listdir('.'):
        if not f.endswith('.table.npy') and not f.endswith('.syn1neg.npy') and not f.endswith('.syn1.npy') and not f.endswith('.syn0.npy'):
            continue
        compress(f)
        os.remove(f)


if __name__ == '__main__':
    main()
