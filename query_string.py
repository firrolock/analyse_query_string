
def analyse(str_src):
    str_dest = str_src[:];
    str_final = "";
    i = 0;
    j = 0;
    flag = 0;
    #print("len(str): %d."%len(str_dest));
    while i <= len(str_dest) - 1:
        if str_dest[i] == ' ' or str_dest[i] == '\n' or str_dest[i] == '\t' or str_dest[i] == '\v':
            i += 1;
            continue;
        j = i;
        if flag == 0:
            while str_dest[j] != ':' and str_dest[j] != '：':
                j += 1;
            str_final += "    \"" + str_dest[i:j] + "\"" + ": ";
            flag = 1;
        elif flag == 1:
            while j <= len(str_dest) - 1 and str_dest[j] != ' ' and str_dest[j] != '\n' and str_dest[j] != '\t' and str_dest[j] != '\v':
                j += 1;
            str_final += "\"" + str_dest[i:j] + "\"" + ",\n";
            flag = 0;
        i = j + 1;
    return str_final;

def input_str():
    print("enter the string you want to transform which must be ':' split: ");
    print("example: type: string");
    string = input();
    return string;

def get_str(pathname):
    f = open(pathname, "r");
    string = f.read();
    f.close();
    return string;

def output_str(string):
    str_dest = analyse(string);
    print("the target string is shown as below: \n");
    print(str_dest);
    print();

def main():
    print("***Query string transformation***");
    while True:
        string = input_str();
        #string = get_str("string_params.txt");  #the default file to extract string is "string_params.txt"
        output_str(string);
        choice = input("enter 'q' to quit or any key to continue: ");
        if choice == 'q':
            break;

if __name__ == "__main__":
    main();
