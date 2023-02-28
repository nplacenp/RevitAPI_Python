
import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from System.Windows.Forms import *
from System.Drawing import *

def SingleComboBoxForm(CBLIST,TITLE):
    form1 = Form()
    form1.Text = TITLE[0]
	
    button1 = Button()
    button1.Text = "Ok"
    button1.DialogResult = DialogResult.Yes
    button1.Location = Point(20,120)

    label1 = Label()
    label1.Location = Point(20,80)
    label1.Text = TITLE[1]

    combo = ComboBox()
    for a in CBLIST:
        combo.Items.Add(a)
    combo.Location = Point(20,30)
    combo.Size = Size(200,20)
	
    form1.FormBorderStyle = FormBorderStyle.FixedToolWindow
    form1.StartPosition = FormStartPosition.CenterScreen
    form1.AcceptButton = button1
	
    form1.Controls.Add(label1)
    form1.Controls.Add(button1) 
    form1.Controls.Add(combo)
	
    form1.Size = Size(260,200)
    form1.ShowDialog()
    return combo.SelectedItem

def multipleComboBoxForm(NAMES,CBLIST,TITLE):
    form1 = Form()
    form1.Text = TITLE	   

    labels=[]
    for a in range(len(NAMES)):
        label1 = Label()
        label1.Text = NAMES[a]
        label1.Location = Point(20,10+a*50)
        label1.Size = Size(400,20)
        labels.append(label1)

    combos=[]
    for a in range(len(CBLIST)):
        combo = ComboBox()
        for b in CBLIST[a]:
            combo.Items.Add(b)
        combo.Name = "Combo"
        combo.Location = Point(20,30+(a*50))
        combo.Size = Size(200,20)
        combos.append(combo)

    button1 = Button()
    button1.Text = "Ok"
    button1.DialogResult = DialogResult.Yes
    button1.Location = Point(20,40+(len(CBLIST)*50))
    
    form1.FormBorderStyle = FormBorderStyle.FixedToolWindow
    form1.StartPosition = FormStartPosition.CenterScreen
    form1.AcceptButton = button1
	
    for a in labels:
        form1.Controls.Add(a)
    for a in combos:
        form1.Controls.Add(a)

    form1.Controls.Add(button1)    
	
    form1.Size = Size(460,120+(len(CBLIST)*50))
    form1.ShowDialog()
    results=[]
    listofvalues = form1.Controls.Find("Combo",True)

    for a in listofvalues:
        results.append(a.SelectedItem)

    return results

def SingleRadioButtonsForm(CBLIST,TITLE):
    form1 = Form()
    form1.Text = TITLE
	
    button1 = Button()
    button1.Text = "Ok"
    button1.DialogResult = DialogResult.Yes
    button1.Location = Point(20,30+(len(CBLIST)*30))

    groupBox1 = GroupBox()
    groupBox1.Name = "Group"
    groupBox1.Text = "Selected Level"

    radiobuttons=[]
    for a in range(len(CBLIST)):
        rb1 = RadioButton()
        rb1.Location = Point(20,20+(a*30))
        rb1.Size = Size(200,20)
        rb1.Name = "Option"
        rb1.Text  = CBLIST[a]
        radiobuttons.append(rb1)

    for a in radiobuttons:
        groupBox1.Controls.Add(a)
	
    form1.FormBorderStyle = FormBorderStyle.FixedToolWindow
    form1.StartPosition = FormStartPosition.CenterScreen
    form1.AcceptButton = button1
	
    form1.Controls.Add(button1) 
    form1.Controls.Add(groupBox1)
	
    form1.Size = Size(260,100+(len(CBLIST)*30))
    form1.ShowDialog()
    results=[]
    listofvalues = groupBox1.Controls.Find("Option",True)
    result = "value"
    for a in listofvalues:
        if a.Checked:
            result = a.Text

    return result