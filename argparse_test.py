import argparse

def main(args):
    print(args.epoch, args.batch_size)

    with open(args.save_path, "xt") as f:
        f.write(f'Arg Epoch is {args.epoch}, and Batch Size is {args.batch_size}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--batch_size', 
                        type=int, 
                        default=32, 
                        help="Batch Size 설정")
    parser.add_argument('--epoch', 
                        type=int, 
                        default=50,
                        help="Epoch 설정")
    parser.add_argument('--save_path',
                        help="저장 경로 설정")

    args = parser.parse_args()

    main(args)