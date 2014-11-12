from project_module import project_object, image_object, link_object, challenge_object

p = project_object('recolourer', 'Recolourer')
p.domain = 'http://www.aidansean.com/'
p.path = 'ROOT_colors'
p.preview_image_ = image_object('http://placekitten.com.s3.amazonaws.com/homepage-samples/408/287.jpg', 408, 287)
p.github_repo_name = 'ROOT_colors'
p.mathjax = True
p.links.append(link_object('http://root.cern.ch/', 'root/html/TColor.html', 'ROOT page'))
p.introduction = 'This project creates an infographic showing the ROOT colors and how they relate to each other.'
p.overview = '''Physicists use ROOT to make plots and it's often useful to be able to easily browse the color space.  ROOT provides a color wheel, but I find the rectangular display very useful as well.  In principle, colors in the same column should suit each other, which makes the rectangular display more useful than the color wheel.'''
