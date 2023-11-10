import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql


def f_szavazo_frame() :
    def get():
        if e_szID.get() == '' :
            messagebox.showinfo("Hiba", "Azonosító mező kötelező!")
        else:
            # Reset entries
            e_vnev.delete(0, 'end'); e_knev.delete(0, 'end'); om_val.set('')

            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('select * from szavazó where szID={}'.format(e_szID.get()))
            rows = cursor.fetchmany(1)
            for row in rows:
                e_vnev.insert(0, row[1])
                e_knev.insert(0, row[2])
                om_val.set(row[3])
            con.close()
            lb_update()


    def insert():
        if e_szID.get() == '' or e_vnev.get() == '' or e_knev.get() == '' or om_val.get() == 'Körzet' :
            messagebox.showinfo("Info", "Minden mező kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('insert into szavazó values("{}","{}","{}","{}")'.format(e_szID.get(), e_vnev.get(), e_knev.get(), eval(om_val.get())[0])) # om_val -> tuple
            cursor.execute('commit')
            # Reset entries
            e_szID.delete(0, 'end'); e_vnev.delete(0, 'end'); e_knev.delete(0, 'end'); om_val.set('Körzet')
            messagebox.showinfo('Info', 'Sikeres beszúrás')
            con.close()
            lb_update()


    def delete():
        if e_szID.get() == '' :
            messagebox.showinfo("Info", "Azonosító mező kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('delete from szavazó where szID="{}"'.format(e_szID.get()))
            cursor.execute('commit')
            # Reset entries
            e_szID.delete(0, 'end'); e_vnev.delete(0, 'end'); e_knev.delete(0, 'end'); om_val.set('Körzet')
            messagebox.showinfo('Info', 'Törlés végrehajtva')
            con.close()
            lb_update()


    def update():
        if e_szID.get() == '' or e_vnev.get() == '' or e_knev.get() == '' or om_val.get() == 'Körzet' :
            messagebox.showinfo("Hiba", "Minden mező kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('update szavazó set vnev="{}", knev="{}", kID="{}" where szID={}'.format(e_vnev.get(), e_knev.get(), eval(om_val.get())[0], e_szID.get()))  # om_val -> tuple
            cursor.execute('commit')
            # Reset entries
            e_szID.delete(0, 'end'); e_vnev.delete(0, 'end'); e_knev.delete(0, 'end'); om_val.set('')
            messagebox.showinfo('Info', 'Sikeres frissítés')
            con.close()
            lb_update()


    def lb_update():
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from szavazó')
        rows = cursor.fetchall()
        lb.delete(0, lb.size())
        for row in rows:
            insertData = '{} - {} {} {}'.format(row[0], row[1], row[2], row[3])
            lb.insert(lb.size() + 1, insertData)
        con.close()
    
    hide_frames()
    szavazo_frame.pack(fill='both', expand=1)

    szID = tk.Label(szavazo_frame, text='Azonosító', font=('bold', 10)).place(x=20, y=30)
    e_szID = tk.Entry(szavazo_frame)
    e_szID.place(x=150, y=30)

    vnev = tk.Label(szavazo_frame, text='Vezetéknév', font=('bold', 10)).place(x=20, y=60)
    e_vnev = tk.Entry(szavazo_frame)
    e_vnev.place(x=150, y=60)

    knev = tk.Label(szavazo_frame, text='Keresztnév', font=('bold', 10)).place(x=20, y=90)
    e_knev = tk.Entry(szavazo_frame)
    e_knev.place(x=150, y=90)

    kID = tk.Label(szavazo_frame, text='Körzet', font=('bold', 10)).place(x=20, y=120)
    
    def om_update() :
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from körzet order by kID')
        kID_list = cursor.fetchall()
        con.close()
        return kID_list

    kID_list = om_update()
    om_val = StringVar(szavazo_frame, 'Körzet')

    om_kID = OptionMenu(szavazo_frame, om_val, *kID_list)
    om_kID.place(x=150, y=120)

    insert_button = tk.Button(szavazo_frame, text="Beszúr", font=('italic', 10), bg="white", command=insert).place(x=20, y=170)
    update_button = tk.Button(szavazo_frame, text="Frissít", font=('italic', 10), bg="white", command=update).place(x=80, y=170)
    delete_button = tk.Button(szavazo_frame, text="Töröl", font=('italic', 10), bg="white", command=delete).place(x=140, y=170)
    get_button = tk.Button(szavazo_frame,    text="Lekér", font=('italic', 10), bg="white", command=get).place(x=190, y=170)

    lb = tk.Listbox(szavazo_frame)
    lb.place(x=290, y=30)
    lb_update()


def f_korzet_frame() :
    def insert():
        if e_kID.get() == '' or e_korzet_nev.get() == '' :
            messagebox.showinfo("Info", "Minden mező kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('insert into körzet values("{}","{}")'.format(e_kID.get(), e_korzet_nev.get()))
            cursor.execute('commit')
            # Reset entries
            e_kID.delete(0, 'end'); e_korzet_nev.delete(0, 'end')
            messagebox.showinfo('Info', 'Sikeres beszúrás')
            con.close()
            lb_update()


    def delete():
        if e_kID.get() == '' :
            messagebox.showinfo("Info", "Azonosító mező kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('delete from körzet where kID="{}"'.format(e_kID.get()))
            cursor.execute('commit')
            # Reset entries
            e_kID.delete(0, 'end'); e_korzet_nev.delete(0, 'end')
            messagebox.showinfo('Info', 'Törlés végrehajtva')
            con.close()
            lb_update()


    def update():
        if e_kID.get() == '' or e_korzet_nev.get() == '' :
            messagebox.showinfo("Hiba", "Minden mező kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('update körzet set korzet_nev="{}" where kID={}'.format(e_korzet_nev.get(), e_kID.get()))
            cursor.execute('commit')
            # Reset entries
            e_kID.delete(0, 'end'); e_korzet_nev.delete(0, 'end')
            messagebox.showinfo('Info', 'Sikeres frissítés')
            con.close()
            lb_update()


    def lb_update():
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from körzet order by kID')
        rows = cursor.fetchall()
        lb.delete(0, lb.size())
        for row in rows:
            insertData = '{} - {}'.format(row[0], row[1])
            lb.insert(lb.size() + 1, insertData)
        con.close()
    
    hide_frames()
    korzet_frame.pack(fill='both', expand=1)

    kID = tk.Label(korzet_frame, text='Azonosító', font=('bold', 10)).place(x=20, y=30)
    e_kID = tk.Entry(korzet_frame)
    e_kID.place(x=150, y=30)

    korzet_nev = tk.Label(korzet_frame, text='Körzet neve', font=('bold', 10)).place(x=20, y=60)
    e_korzet_nev = tk.Entry(korzet_frame)
    e_korzet_nev.place(x=150, y=60)

    insert_button = tk.Button(korzet_frame, text="Beszúr", font=('italic', 10), bg="white", command=insert).place(x=20, y=100)
    update_button = tk.Button(korzet_frame, text="Frissít", font=('italic', 10), bg="white", command=update).place(x=80, y=100)
    delete_button = tk.Button(korzet_frame, text="Töröl", font=('italic', 10), bg="white", command=delete).place(x=140, y=100)

    lb = tk.Listbox(korzet_frame)
    lb.place(x=290, y=30)
    lb_update()


def f_jelolt_frame() :
    def insert():
        if om_szID_val.get() == 'Szavazó' :
            messagebox.showinfo("Info", "Minden mező kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('insert into jelölt (szID) values ("{}")'.format(om_szID_val.get()[:2]))
            cursor.execute('commit')
            # Reset entries
            om_szID_val.set('Szavazó')
            messagebox.showinfo('Info', 'Sikeres beszúrás')
            con.close()
            lb_update()


    def delete():
        if lb.curselection() == () :
            messagebox.showinfo("Info", "Kattintson a listában szereplő törölni kívánt jelöltre!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('delete from jelölt where jID="{}"'.format(lb.get(lb.curselection())[:2]))
            cursor.execute('commit')
            # Reset entries
            om_szID_val.set('Szavazó')
            messagebox.showinfo('Info', 'Törlés végrehajtva')
            con.close()
            lb_update()


    def lb_update():
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select jelölt.jID, szavazó.vnev, szavazó.knev from jelölt inner join szavazó on szavazó.szID=jelölt.szID order by jelölt.jID')
        rows = cursor.fetchall()
        lb.delete(0, lb.size())
        for row in rows:
            insertData = '{} - {} {}'.format(row[0], row[1], row[2])
            lb.insert(lb.size() + 1, insertData)
        con.close()
    
    hide_frames()
    jelolt_frame.pack(fill='both', expand=1)

    szID = tk.Label(jelolt_frame, text='Szavazó', font=('bold', 10)).place(x=20, y=60)
    
    def om_update() :
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select szavazó.szID, szavazó.vnev, szavazó.knev from szavazó')
        rows = cursor.fetchall()
        szID_list = list()
        for row in rows :
            update_data = str(row[0]) + ' - ' + row[1] + ' ' + row[2]
            szID_list.append(update_data)
        con.close()
        return szID_list

    szID_list = om_update()
    om_szID_val = StringVar(jelolt_frame, 'Szavazó')
    
    om_szID = OptionMenu(jelolt_frame, om_szID_val, *szID_list)
    om_szID.place(x=150, y=60)

    insert_button = tk.Button(jelolt_frame, text="Beszúr", font=('italic', 10), bg="white", command=insert).place(x=150, y=100)
    delete_button = tk.Button(jelolt_frame, text="Töröl", font=('italic', 10), bg="white", command=delete).place(x=210, y=100)

    lb = tk.Listbox(jelolt_frame, width=25, height=6, selectmode=SINGLE)
    lb.place(x=290, y=30)
    lb_update()


def f_szavazas_frame() :
    def insert():
        if e_fID.get() == '' :
            messagebox.showinfo("Info", "Azonosító mező kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('insert into szavazás values("{}")'.format(e_fID.get()))
            cursor.execute('commit')
            # Reset entries
            e_fID.delete(0, 'end')
            messagebox.showinfo('Info', 'Sikeres beszúrás')
            con.close()
            lb_update()


    def delete():
        if e_fID.get() == '' :
            messagebox.showinfo("Info", "Azonosító mező kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('delete from szavazás where fID="{}"'.format(e_fID.get()))
            cursor.execute('commit')
            # Reset entries
            e_fID.delete(0, 'end')
            messagebox.showinfo('Info', 'Törlés végrehajtva')
            con.close()
            lb_update()


    def lb_update():
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from szavazás')
        rows = cursor.fetchall()
        lb.delete(0, lb.size())
        for row in rows:
            insertData = '{}. forduló'.format(row[0])
            lb.insert(lb.size() + 1, insertData)
        con.close()
    
    hide_frames()
    szavazas_frame.pack(fill='both', expand=1)

    fID = tk.Label(szavazas_frame, text='Forduló', font=('bold', 10))
    fID.place(x=20, y=30)
    
    e_fID = tk.Entry(szavazas_frame, width=3)
    e_fID.place(x=150, y=30)

    # Wall of modification
    mod = Label(szavazas_frame, text="Módosítok")
    mod.place(x=20, y=60)

    check_val = IntVar()

    def f_check():
        if check_val.get() == 1:    # When checked
            fID.config(fg='black')
            e_fID.config(state=NORMAL)
            insert_button.config(state=NORMAL)
            delete_button.config(state=NORMAL)
        elif check_val.get() == 0:  # When unchecked
            fID.config(fg='gray')
            e_fID.config(state=DISABLED)
            insert_button.config(state=DISABLED)
            delete_button.config(state=DISABLED)

    check = Checkbutton(szavazas_frame, variable=check_val, command=f_check)
    check.place(x=150, y=60)

    insert_button = tk.Button(szavazas_frame, text="Beszúr", font=('italic', 10), bg="white", command=insert)
    insert_button.place(x=150, y=100)
    delete_button = tk.Button(szavazas_frame, text="Töröl", font=('italic', 10), bg="white", command=delete)
    delete_button.place(x=210, y=100)

    # Modification default disabled
    f_check()

    lb = tk.Listbox(szavazas_frame, width=25, height=6)
    lb.place(x=290, y=30)
    lb_update()


def f_szavaz_frame() :
    def insert():
        if om_szID_val.get() == 'Szavazó' or om_jID_val.get() == 'Jelölt' or om_fID_val.get() == 'Forduló' :
            messagebox.showinfo("Info", "Minden mező kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('insert into szavaz values("{}","{}","{}")'.format(eval(om_szID_val.get())[0], eval(om_jID_val.get())[0], eval(om_fID_val.get())[0])) # om_val -> tuple
            cursor.execute('commit')
            # Reset entries
            om_szID_val.set('Szavazó'); om_jID_val.set('Jelölt'); om_fID_val.set('Forduló')
            messagebox.showinfo('Info', 'Sikeres beszúrás')
            con.close()
            lb_update()


    def delete():
        if lb.curselection() == () :
            messagebox.showinfo("Info", "Kattintson a listában szereplő törölni kívánt szavazatra!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('delete from szavaz where szID="{}" and fID="{}"'.format(lb.get(lb.curselection())[:2], lb.get(lb.curselection())[-10]))
            cursor.execute('commit')
            messagebox.showinfo('Info', 'Törlés végrehajtva')
            con.close()
            lb_update()


    def lb_update():
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select szavazó.szID, szavazó.vnev, szavazó.knev, fID from szavaz inner join szavazó on szavazó.szID=szavaz.szID order by szavazó.szID')
        rows = cursor.fetchall()
        lb.delete(0, lb.size())
        for row in rows:
            insertData = '{} {} {} -> {}. forduló'.format(row[0], row[1], row[2], row[3])
            lb.insert(lb.size() + 1, insertData)
        con.close()
    
    hide_frames()
    szavaz_frame.pack(fill='both', expand=1)

    szID = tk.Label(szavaz_frame, text='Szavazó', font=('bold', 10)).place(x=20, y=30)
    def om_szID_update() :
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select szID, vnev, knev from szavazó order by szID')
        szID_list = cursor.fetchall()
        con.close()
        return szID_list
    szID_list = om_szID_update()
    om_szID_val = StringVar(szavaz_frame, 'Szavazó')
    om_szID = OptionMenu(szavaz_frame, om_szID_val, *szID_list)
    om_szID.place(x=150, y=30)

    jID = tk.Label(szavaz_frame, text='Jelölt', font=('bold', 10)).place(x=20, y=60)
    def om_jID_update() :
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select jelölt.jID, szavazó.vnev, szavazó.knev from jelölt inner join szavazó on szavazó.szID=jelölt.szID order by jelölt.jID')
        jID_list = cursor.fetchall()
        con.close()
        return jID_list
    jID_list = om_jID_update()
    om_jID_val = StringVar(szavaz_frame, 'Jelölt')
    om_jID = OptionMenu(szavaz_frame, om_jID_val, *jID_list)
    om_jID.place(x=150, y=60)

    fID = tk.Label(szavaz_frame, text='Forduló', font=('bold', 10)).place(x=20, y=90)
    def om_fID_update() :
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select fID from szavazás')
        jID_list = cursor.fetchall()
        con.close()
        return jID_list
    fID_list = om_fID_update()
    om_fID_val = StringVar(szavaz_frame, 'Forduló')
    om_fID = OptionMenu(szavaz_frame, om_fID_val, *fID_list)
    om_fID.place(x=150, y=90)

    insert_button = tk.Button(szavaz_frame, text="Beszúr", font=('italic', 10), bg="white", command=insert).place(x=150, y=130)
    delete_button = tk.Button(szavaz_frame, text="Töröl", font=('italic', 10), bg="white", command=delete).place(x=210, y=130)

    lb = tk.Listbox(szavaz_frame, width=30)
    lb.place(x=290, y=30)
    lb_update()


def f_indul_frame() :
    def insert():
        if om_jID_val.get() == 'Jelölt' or om_fID_val.get() == 'Szavazó' :
            messagebox.showinfo("Info", "Minden mező kötelező!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('insert into indul values("{}","{}")'.format(eval(om_jID_val.get())[0], eval(om_fID_val.get())[0]))
            cursor.execute('commit')
            # Reset entries
            om_jID_val.set('Jelölt'); om_fID_val.set('Szavazó')
            messagebox.showinfo('Info', 'Sikeres beszúrás')
            con.close()
            lb_update()


    def delete():
        if lb.curselection() == () :
            messagebox.showinfo("Info", "Kattintson a listában szereplő törölni kívánt jelöltre!")
        else:
            con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
            cursor = con.cursor()
            cursor.execute('delete from indul where jID="{}"'.format(lb.get(lb.curselection())[:2]))
            cursor.execute('commit')
            # Reset entries
            om_jID_val.set('Jelölt'); om_fID_val.set('Szavazó')
            messagebox.showinfo('Info', 'Törlés végrehajtva')
            con.close()
            lb_update()


    def lb_update():
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select jelölt.jID, szavazó.vnev, szavazó.knev, indul.fID from indul inner join jelölt on indul.jID=jelölt.jID inner join szavazó on jelölt.szID=szavazó.szID')
        rows = cursor.fetchall()
        lb.delete(0, lb.size())
        for row in rows:
            insertData = '{} - {} {} -> {}. forduló'.format(row[0], row[1], row[2], row[3])
            lb.insert(lb.size() + 1, insertData)
        con.close()
    
    hide_frames()
    indul_frame.pack(fill='both', expand=1)

    # jID
    jID = tk.Label(indul_frame, text='Jelölt azonosító', font=('bold', 10)).place(x=20, y=30)

    def om_jID_update() :
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select jelölt.jID, szavazó.vnev, szavazó.knev from jelölt left join szavazó on szavazó.szID=jelölt.szID')
        jID_list = cursor.fetchall()
        con.close()
        return jID_list

    jID_list = om_jID_update()
    om_jID_val = StringVar(indul_frame, 'Jelölt')
    
    om_jID = OptionMenu(indul_frame, om_jID_val, *jID_list)
    om_jID.place(x=150, y=30)

    # fID
    fID = tk.Label(indul_frame, text='Forduló', font=('bold', 10)).place(x=20, y=60)
    
    def om_fID_update() :
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select * from szavazás')
        szID_list = cursor.fetchall()
        con.close()
        return szID_list

    fID_list = om_fID_update()
    om_fID_val = StringVar(indul_frame, 'Forduló')
    
    om_fID = OptionMenu(indul_frame, om_fID_val, *fID_list)
    om_fID.place(x=150, y=60)

    insert_button = tk.Button(indul_frame, text="Beszúr", font=('italic', 10), bg="white", command=insert).place(x=150, y=100)
    delete_button = tk.Button(indul_frame, text="Töröl", font=('italic', 10), bg="white", command=delete).place(x=210, y=100)

    lb = tk.Listbox(indul_frame, width=30, height=6, selectmode=SINGLE)
    lb.place(x=290, y=30)
    lb_update()


def f_l1_frame() :
    hide_frames()
    l1_frame.pack(fill='both', expand=1)

    def f_l1() :
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select COUNT(szID) from szavazó WHERE kID=(select kID from körzet where korzet_nev = "{}")'.format(l1.get()))
        val = str(cursor.fetchone()[0])
        l1.delete(0, 'end')
        l1.insert(0, val)
        con.close()
    
    tk.Label(l1_frame, text='Melyik körzetben mennyi szavazó tartózkodik', font=('bold', 10)).place(x=20, y=30)
    l1 = tk.Entry(l1_frame)
    l1.place(x=20, y=60)

    l1_button = tk.Button(l1_frame, text="Keresés", font=('italic', 10), bg="white", command=f_l1).place(x=150, y=60)
    

def f_l2_frame() :
    hide_frames()
    l2_frame.pack(fill='both', expand=1)

    def lb_update() :
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select szavazó.vnev, szavazó.knev, count(szavaz.jID) from szavaz inner join jelölt on szavaz.jID=jelölt.jID inner join szavazó on szavazó.szID=jelölt.szID group by jelölt.jID order by COUNT(szavaz.jID) desc')
        rows = cursor.fetchall()
        lb.delete(0, lb.size())
        for row in rows:
            insertData = '{} {} : {}'.format(row[0], row[1], row[2])
            lb.insert(lb.size() + 1, insertData)
        con.close()
    
    tk.Label(l2_frame, text='Jelöltek szavazatai', font=('bold', 10)).place(x=20, y=30)
    lb_button = tk.Button(l2_frame, text="Frissít", font=('italic', 10), bg="white", command=lb_update).place(x=20, y=235)

    lb = tk.Listbox(l2_frame)
    lb.place(x=20, y=60)
    lb_update()
    

def f_l3_frame() :
    hide_frames()
    l3_frame.pack(fill='both', expand=1)

    def lb_update() :
        con = mysql.connect(host=dbhost, user=dbuser, password=dbpass, database=dbname)
        cursor = con.cursor()
        cursor.execute('select körzet.korzet_nev, count(szavaz.szID) from szavazó left join szavaz on szavazó.szID=szavaz.szID inner join körzet on körzet.kID=szavazó.kID group by szavazó.kID order by COUNT(szavaz.szID) desc')
        rows = cursor.fetchall()
        lb.delete(0, lb.size())
        for row in rows:
            insertData = '{} : {}'.format(row[0], row[1])
            lb.insert(lb.size() + 1, insertData)
        con.close()
    
    tk.Label(l3_frame, text='Körzeten belül hány szavazat érkezett összesen', font=('bold', 10)).place(x=20, y=30)
    lb_button = tk.Button(l3_frame, text="Frissít", font=('italic', 10), bg="white", command=lb_update).place(x=20, y=235)

    lb = tk.Listbox(l3_frame)
    lb.place(x=20, y=60)
    lb_update()
    

def hide_frames() :
    szavazo_frame.pack_forget()
    korzet_frame.pack_forget()
    jelolt_frame.pack_forget()
    szavazas_frame.pack_forget()
    szavaz_frame.pack_forget()
    indul_frame.pack_forget()
    l1_frame.pack_forget()
    l2_frame.pack_forget()
    l3_frame.pack_forget()


if __name__ == '__main__' :
    # Data for connecting with MySQL DB
    dbhost = 'localhost'
    dbname = "szavazatszámláló"
    dbuser = 'root'
    dbpass = ''

    # Create main window and customisations
    root = tk.Tk()
    root.title('Szavazatszámláló')
    root.iconbitmap('szavazatszámláló\icon.ico')
    root.geometry('500x500')

    # Create menu bar and make root use menu_bar
    menu_bar = Menu(root)
    root.config(menu=menu_bar)

    # Create a menu widget
    t_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Táblák', menu=t_menu)

    # Create frames for menu widget
    szavazo_frame   = Frame(root)
    korzet_frame    = Frame(root)
    jelolt_frame    = Frame(root)
    szavazas_frame  = Frame(root)
    szavaz_frame    = Frame(root)
    indul_frame     = Frame(root)

    # Add items to the menu widget
    t_menu.add_command(label='Szavazó',     command=f_szavazo_frame)
    t_menu.add_command(label='Körzet',      command=f_korzet_frame)
    t_menu.add_command(label='Jelölt',      command=f_jelolt_frame)
    t_menu.add_command(label='Szavazás',    command=f_szavazas_frame)
    t_menu.add_command(label='Szavaz',      command=f_szavaz_frame)
    t_menu.add_command(label='Indul',       command=f_indul_frame)

    # Create a menu widget
    l_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Lekérdezések', menu=l_menu)

    # Create frames for menu widget
    l1_frame    = Frame(root)
    l2_frame    = Frame(root)
    l3_frame    = Frame(root)

    # Add items to the menu widget
    l_menu.add_command(label='1. lekérdezés',       command=f_l1_frame)
    l_menu.add_command(label='2. lekérdezés',       command=f_l2_frame)
    l_menu.add_command(label='3. lekérdezés',       command=f_l3_frame)


    root.mainloop()