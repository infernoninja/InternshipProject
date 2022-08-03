from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#create instance of webdriver and open webpage
driver = webdriver.Chrome()
time.sleep(1.5)
#open netsuite case list
driver.get("""sensitive info""") 
time.sleep(2.5)
#login
email = driver.find_element(By.ID, "email")
email.send_keys("""sensitive info""")
password = driver.find_element(By.ID, "password")
password.send_keys("""sensitive info""")
time.sleep(.2)
driver.find_element(By.XPATH, "//*[@id= 'login-submit']").click()
#check if user is done logging in and putting in verification code and got to a case
print('Are you done putting in ur verification code and have you clicked done and clicked on a case? (y for yes)')
user_in_user_pass_2fa_gottocase = input()
if (user_in_user_pass_2fa_gottocase ==  'y'):
    time.sleep(5)

###  Very specific cases to check
str_doc = "Document Processing Error"
str_data = "Data Processing Error"
str_sps = "SPS Commerce received NetSuite Error Notification"
str_FI = "Error: FI"
str_AP_docs = """sensitive info"""
str_import = "Import Errors"
###   Names
name_B = """sensitive info, variable is shortened"""
name_H = """sensitive info, variable is shortened"""
name_M = """sensitive info, variable is shortened"""
name_K = """sensitive info, variable is shortened"""
###   Case Issues
nsd = "NS Dashboards"
nsop = "NS Order Processing"
nsi = "NS Inventory"
nsp = "NS Purchasing"
nsahp = "NS Acct, HR, Payroll"
nspro = "NS Projects"
nswms = "NS WMS"
edi = "EDI"
v = "Valogix"
os = "Other System"
nsrp = "NS Role/Permission"
###  Case Types
i = "Incident"
r = "Request"
e = "Enhancement"
p = "Project"
###  Email checking
str_email_ac = """sensitive info"""
###   loop techinal stuff
bool_while_loop = True
fifty_count = 0

while(bool_while_loop) :

    #check booleans for while loop and changes
    changes_bool = False
    check_case_for_changes = False
    ### webelements are dynamic and mutable ###
    #case title string
    title_str = driver.find_element(By.CLASS_NAME, "uir-page-title-secondline").__getattribute__("text")
    #get email string
    email_str = driver.find_element(By.XPATH, "//*[@name= 'email']").get_attribute('value')
    #get requester webelement
    requestor_str = driver.find_element(By.XPATH, "//*[@name= 'company_display']")
    #get assigned to web element
    assigned_str = driver.find_element(By.XPATH, "//*[@name= 'inpt_assigned']")
    #get case issue webelemet
    case_issue_str = driver.find_element(By.XPATH, "//*[@name= 'inpt_issue']")
    #get case type webelement
    case_type_str = driver.find_element(By.XPATH, "//*[@name= 'inpt_category']")
    #get dropdown button web element
    dropdown_button = driver.find_element(By.XPATH, "//*[@alt= 'More Options']")
    #get next arrow botton web element
    next_arrow_button = driver.find_element(By.XPATH, "//*[@src= '/uirefresh/img/arrow_right.png']")
    #values to check for manual cases
    before_assigned_str = assigned_str.get_attribute('value')
    before_case_issue_str = case_issue_str.get_attribute('value')
    before_case_type_str = case_type_str.get_attribute('value')

    #check for very specifc cases ()   
    if (str_doc in title_str) or (str_data in title_str) or (str_sps in title_str) or (str_FI in title_str) or (str_AP_docs in title_str) or (str_import in title_str):

        if (assigned_str.get_attribute('value') == ' '):
            assigned_str.send_keys(name_H)
            changes_bool = True 

        if (case_issue_str.get_attribute('value') == ' '):
            if (str_import in title_str):
                case_issue_str.send_keys(v)
            else:
                case_issue_str.send_keys(edi)
            changes_bool = True
            
        if (case_type_str.get_attribute('value') == ' '):
            case_type_str.send_keys(i)
            changes_bool = True

        if changes_bool:
                driver.execute_script("window.scrollTo(0,0)")
                dropdown_button.click()
                time.sleep(1)
                save_next_button = driver.find_element(By.CSS_SELECTOR,"a[href*=submitnext]" )
                time.sleep(.2)
                save_next_button.click()
        else:
            driver.execute_script("window.scrollTo(0,0)")
            next_arrow_button.click()
            time.sleep(3)
    #for any other case
    else:
        check_case_for_changes = True
        if (requestor_str.get_attribute("value") == "Anonymous Customer"):
            if str_email_ac in email_str:
                period_index = email_str.index(".")
                at_index = email_str.index("@")
                first_name = email_str[0:period_index]
                last_name = email_str[(period_index + 1):at_index]
                full_name = first_name + " " + last_name
                for i in range(1,19):
                    requestor_str.send_keys('\ue003')
                requestor_str.send_keys(full_name)
                changes_bool = True

        if (assigned_str.get_attribute('value') == ' '):
            print("who is it assigned to? h for heidi, b for brady, m for meha, or k for kelsey or enter a name")
            user_in_change_asgn = input()
            if (user_in_change_asgn == "h"):
                assigned_str.send_keys(name_H)
            elif (user_in_change_asgn == "m"):
                assigned_str.send_keys(name_M)
            elif (user_in_change_asgn == "b"):
                assigned_str.send_keys(name_B)
            elif (user_in_change_asgn == "k"):
                assigned_str.send_keys(name_K)
            elif (user_in_change_asgn == ""):
                pass
            else:
                assigned_str.send_keys(user_in_change_asgn)
        
        if (case_issue_str.get_attribute('value') == ' '):
            print("case issue? \nnsd = 'NS Dashboards'\nnsop = 'NS Order Processing'\nnsi = 'NS Inventory'\nnsp = 'NS Purchasing'\nnsahp = 'NS Acct, HR, Payroll'\nnspro = 'NS Projects'\nnswms = 'NS WMS'\nedi = 'EDI'\nv = 'Valogix'\nos = 'Other System'\nnsrp = 'NS Role/Permission'")
            user_in_change_iss = input()
            if (user_in_change_iss == "nsd"):
                case_issue_str.send_keys(nsd)
            elif (user_in_change_iss == "nsop"):
                case_issue_str.send_keys(nsop)
            elif (user_in_change_iss == "nsi"):
                case_issue_str.send_keys(nsi)
            elif (user_in_change_iss == "nsp"):
                case_issue_str.send_keys(nsp)
            elif (user_in_change_iss == "nsahp"):
                case_issue_str.send_keys(nsahp)
            elif (user_in_change_iss == "nspro"):
                case_issue_str.send_keys(nspro)
            elif (user_in_change_iss == "nswms"):
                case_issue_str.send_keys(nswms)
            elif (user_in_change_iss == "edi"):
                case_issue_str.send_keys(edi)
            elif (user_in_change_iss == "v"):
                case_issue_str.send_keys(v)
            elif (user_in_change_iss == "os"):
                case_issue_str.send_keys(os)
            elif (user_in_change_iss == "nsrp"):
                case_issue_str.send_keys(nsrp)
            else:
                pass

        if (case_type_str.get_attribute('value') == " "):
            print("case type? (incident = i, request = r, enhancement = e, project = p")
            user_in_change_type = input()
            if (user_in_change_type == "i"):
                case_type_str.send_keys(i)
            elif (user_in_change_type == "r"):
                case_type_str.send_keys(r)
            elif (user_in_change_type == "e"):
                case_type_str.send_keys(e)
            elif (user_in_change_type == "p"):
                case_type_str.send_keys(p)
            else:
                pass

        if check_case_for_changes:
            after_assigned_str = assigned_str.get_attribute('value')            
            after_case_issue_str = case_issue_str.get_attribute('value')
            after_case_type_str = case_type_str.get_attribute('value')
            if(after_assigned_str != before_assigned_str):
                changes_bool = True
            if (after_case_issue_str != before_case_issue_str):
                changes_bool = True 
            if (after_case_type_str != before_case_type_str):
                changes_bool = True
        if changes_bool:
            driver.execute_script("window.scrollTo(0,0)")
            dropdown_button.click()
            time.sleep(1)
            save_next_button = driver.find_element(By.CSS_SELECTOR,"a[href*=submitnext]" )
            time.sleep(.2)
            save_next_button.click()
            time.sleep(1.5)
        else:
            driver.execute_script("window.scrollTo(0,0)")
            next_arrow_button.click()
            time.sleep(1.5)
    #feeling tired? then end your misery
    fifty_count += 1
    if (fifty_count == 50):
        print("done for now? (y)")
        user_in_fifty = input()
        if (user_in_fifty == "y"):
            bool_while_loop = False
        fifty_count = 0