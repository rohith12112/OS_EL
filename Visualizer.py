import tkinter as tk

root = tk.Tk()
root.geometry("500x400")
root.title("Page Replacement Algorithm Visualization")

def fifo_algorithm(num_pages, pages, num_frames,root):
    frames = [-1] * num_frames
    page_faults = 0
    hits = 0
    frame_pointer = 0
    root.title("FIFO Algorithm")
    root.configure(background="black")

    for i in range(num_pages):
        page = pages[i]
        label=tk.Label(root,text=f"{pages[i]}",font="bold",bd=2,fg="white",bg="black",relief=tk.SOLID)
        label.grid(row=6, column=1+i, ipadx=20, ipady=10, sticky=tk.W)
        page_found = False

        # Check if page is already in memory
        for j in range(num_frames):
            if frames[j] == page:
                page_found = True
                hits += 1
                break

        # If page is not in memory, replace oldest page with new page
        if not page_found:
            frames[frame_pointer] = page
            frame_pointer = (frame_pointer + 1) % num_frames
            page_faults += 1

        # Print current state of frames
        for j in range(num_frames):
            if frames[j] == -1:
                
                if not page_found:
                    # page fault
                    label=tk.Label(root,text="  ",font = "blod",bd=2,bg="#ff0000",relief=tk.SOLID)
                    label.grid(row=7+j, column=1+i, ipadx=20, ipady=10, sticky=tk.W)

                else:
                    label=tk.Label(root,text="  ",font = "blod",bg="#00cc00", bd=2,relief=tk.SOLID)
                    label.grid(row=7+j, column=1+i, ipadx=20, ipady=10, sticky=tk.W)
            else:
                if not page_found:
                    label=tk.Label(root,text="%d" % frames[j],font = "blod",bd=2,bg="#ff0000",relief=tk.SOLID)
                    label.grid(row=7+j, column=1+i, ipadx=20, ipady=10, sticky=tk.W)

                else:
                    label=tk.Label(root,text="%d" % frames[j],font = "blod", bg="#00cc00", bd=2,relief=tk.SOLID)
                    label.grid(row=7+j, column=1+i, ipadx=20, ipady=10, sticky=tk.W)
    print("FIFO Algorithm : ")
    print("\nPage Faults: ",page_faults)
    print("\nTotal Hits : ",hits)


def lru_algorithm(num_pages, pages, num_frames,root):
    frames = [-1] * num_frames
    page_faults = 0
    hits = 0
    used = [0] * num_frames
    root.title("LRU Algorithm")
    root.configure(background="black")
    
    for i in range(num_pages):
        page = pages[i]
        label=tk.Label(root,text=f"{pages[i]}",font="bold",bd=2,fg="white",bg="black",relief=tk.SOLID)
        label.grid(row=6, column=1+i, ipadx=20, ipady=10, sticky=tk.W)
        page_found = False

        # Check if page is already in memory
        for j in range(num_frames):
            if frames[j] == page:
                page_found = True
                hits += 1
                used[j] = i
                break

        # If page is not in memory, find least recently used page to replace
        if not page_found:
            # If there is an empty frame, use it
            if -1 in frames:
                frame_to_replace = frames.index(-1)
            else:
                # Otherwise, find least recently used frame to replace
                frame_to_replace = used.index(min(used))
            frames[frame_to_replace] = page
            used[frame_to_replace] = i
            page_faults += 1
            
        # Print current state of frames
        for j in range(num_frames):
            if frames[j] == -1:
                
                if not page_found:

                    label=tk.Label(root,text="  ",font = "blod",bd=2,bg="#ff0000",relief=tk.SOLID)
                    label.grid(row=7+j, column=1+i, ipadx=20, ipady=10, sticky=tk.W)

                else:
                    label=tk.Label(root,text="  ",font = "blod",bg="#00cc00", bd=2,relief=tk.SOLID)
                    label.grid(row=7+j, column=1+i, ipadx=20, ipady=10, sticky=tk.W)
            else:
                
                if not page_found:
                    label=tk.Label(root,text="%d" % frames[j],font = "blod",bd=2,bg="#ff0000",relief=tk.SOLID)
                    label.grid(row=7+j, column=1+i, ipadx=20, ipady=10, sticky=tk.W)

                else:
                    label=tk.Label(root,text="%d" % frames[j],font = "blod",bg="#00cc00", bd=2,relief=tk.SOLID)
                    label.grid(row=7+j, column=1+i, ipadx=20, ipady=10, sticky=tk.W)
    
    print("LRU Algorithm : ")                
    print("\nPage Faults: ",page_faults)
    print("\nTotal Hits : ",hits)

def visualize():

    win=tk.Tk()
    pages = [int(x) for x in pages_entry.get().split()]
    num_frames = int(num_frames_entry.get())
    num_pages = len(pages)
    print("Reference string : ",pages,"\nFrames : ",num_frames)
    
    # Run FIFO page replacement algorithm
    fifo_algorithm(num_pages, pages, num_frames,win)

def visualize_lru():

    win=tk.Tk()
    pages = [int(x) for x in pages_entry.get().split()]
    num_frames = int(num_frames_entry.get())
    num_pages = len(pages)
    print("Reference string : ",pages,"\nFrames : ",num_frames)

    # Run FIFO page replacement algorithm
    lru_algorithm(num_pages, pages, num_frames,win)

def clear_inputs():
    pages_entry.delete(0, tk.END) 
    num_frames_entry.delete(0, tk.END) 
    
# Create input labels and entry widgets
pages_label = tk.Label(root, text="Reference String :")
pages_entry = tk.Entry(root)
num_frames_label = tk.Label(root, text="Number of Frames :")
num_frames_entry = tk.Entry(root)

# Create Buttons
visualize_button = tk.Button(root, text="Visualize FIFO", command=visualize)
visualize_lru_button = tk.Button(root, text="Visualize LRU", command=visualize_lru)
clear_button = tk.Button(root, text="Clear Input", command=clear_inputs)

# Grid layout for input widgets
pages_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
pages_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
num_frames_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
num_frames_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)


# Grid layout for visualize button
visualize_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
visualize_lru_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
clear_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

exp_lbl = tk.Label(root, text="Example Reference String : 1 4 5 1 7 8 3 4 2 1 6 7").grid(row=8, column=0, padx=5, pady=5,sticky=tk.W)
exp_lbl2= tk.Label(root, text="Example Number of Frames : 4").grid(row=9, column=0, padx=5, pady=5,sticky=tk.W)
tk.Label(root, text="Green Represents: Hit").grid(row=10, column=0, padx=5, pady=5,sticky=tk.W)
tk.Label(root, text="Red Represents  : Page Fault").grid(row=11, column=0, padx=5, pady=5,sticky=tk.W)

root.mainloop()