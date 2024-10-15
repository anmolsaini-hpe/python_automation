import subprocess

def image_scane(image_name):
    result=subprocess.run(["trivy","image",image_name],capture_output=True,text=True)
    print(result.stdout)



if __name__=="__main__":
    image_scane("nginx:alpine")
