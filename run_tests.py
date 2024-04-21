import subprocess
import os
import sys

def run_test(case_num, solution_script):
    # 获取 solution_script 的目录
    solution_dir = os.path.dirname(solution_script)
    input_file = os.path.join(solution_dir, f"{case_num}.in.txt")
    output_file = os.path.join(solution_dir, f"{case_num}.out.txt")
    ans_file = os.path.join(solution_dir, f"{case_num}.ans.txt")

    if os.path.exists(input_file) and os.path.exists(ans_file):
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            subprocess.run(["python", solution_script], stdin=infile, stdout=outfile)
        
        with open(output_file, "r") as outfile, open(ans_file, "r") as ansfile:
            output = outfile.read().strip()
            answer = ansfile.read().strip()

            if output == answer:
                print(f"Case {case_num} passed")
            else:
                print(f"Case {case_num} failed, Expect: {answer}, Out: {output}")
    else:
        print(f"Input or answer file for case {case_num} does not exist.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_tests.py <solution_script>")
        sys.exit(1)
    solution_script = sys.argv[1]  # Get the solution script from command line arguments
    case_num = 1
    while True:
        # 使用 solution_script 的目录来检查输入文件
        if not os.path.exists(os.path.join(os.path.dirname(solution_script), f"{case_num}.in.txt")):
            break
        run_test(case_num, solution_script)
        case_num += 1