from flask import Flask, render_template, request, send_file

app = Flask(__name__)

slide = 0
total_slides = 3
registration_url = "https://lu.ma/BTBL"
registration_button_text = "Register"
speakers_button_text = "Speakers"
next_speaker_button_text = "Next Speaker"

# Return one of the slide images, if it exists
@app.route('/<path:subpath>', methods=['GET'])
def image_handler(subpath):
    try:
        return send_file("./assets/" + subpath + ".png")
    except: 
        return "Not found"
    

# Return the correct template for a particlar slide
@app.route('/', methods=['GET', 'POST'])
def frame_handler():
    global slide
    global total_slides
    global next_speaker_button_text
    global registration_button_text
    global speakers_button_text
    global registration_url

    if request.method == 'POST':
        if slide == 1:
            slide += 1
            slide_path = "slide-" + str(slide)
            return render_template("slide-n.html", frame_image=(request.url + slide_path), og_image=(request.url + slide_path), left_button_text="Location"t, left_button_target=request.url, right_button_text=registration_button_text, right_button_target=registration_url)
        if slide == 2:
            slide += 1
            slide_path = "slide-" + str(slide)
            return render_template("slide-n.html", frame_image=(request.url + slide_path), og_image=(request.url + slide_path), left_button_text="Home", left_button_target=request.url, right_button_text=registration_button_text, right_button_target=registration_url)
        else: 
            slide = 0
            slide_path = "slide-" + str(slide)
            return render_template("slide-n.html", frame_image=(request.url + slide_path), og_image=(request.url + slide_path), left_button_text="Schedule", left_button_target=request.url, right_button_text=registration_button_text, right_button_target=registration_url)
    else:
        slide_path = "slide-" + str(slide)
        return render_template("slide-n.html", frame_image=(request.url + slide_path), og_image=(request.url + slide_path), left_button_text=speakers_button_text, left_button_target=request.url, right_button_text=registration_button_text, right_button_target=registration_url)
        
