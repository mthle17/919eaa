import re
import glob

try:
    with open("tasks.txt", "w") as f_out:
        for file in glob.glob("./Exercises/*.py"):
            if not file.startswith("./Exercises\\ex_"):
                continue
            try:
                with open(file, "r") as f_in:
                    content = f_in.read()

                    p = re.compile('(?:""")(.*?)(?:""")', re.DOTALL)
                    result = p.findall(content)

                    if(len(result) == 0):
                        print(f"!FAILED for {file}")
                    
                    comment = result[0].lstrip()
                    f_out.write("-" * 120 + "\n")
                    fileDisplay = file.split("\\")[-1]
                    f_out.write(f"{fileDisplay}\n")
                    f_out.write("-" * 120 + "\n")
                    f_out.write(comment)
                    f_out.flush()
            except Exception as ex:
                print(f"Failed reading from {file}: {ex}")

except Exception as ex:
    print(f"Failed writing to tasks.txt: {ex}")

