# Slicer Coding Challenge

## Setup

You must have python 3 installed.

All of the python requirements are listed in `requirements.txt`.  You can install them using:

    pip install -r requirements.txt

Once you have installed everything, be sure to run the Django migrations, and
to create a super user (so you can login to the admin).  You can do this by running:

    python manage.py migrate
    python manage.py createsuperuser

Now start the Django test server and login as the user you just created, and
navigate to the image series page.  Click the "add" button, and upload one of the sample zip-archives
containing DICOM files.

You should see it in the "home" page of the site (e.g. 127.0.0.1:8000/).

## Overview

There should be one row for each archive you uploaded.  The "View" link in the table doesn't do anything.

In this challenge your job is to create a simple 3D-image-slice viewer.

## Part I - Create Slices

Update `ImageSeries`'s custom save method so that it dumps a set of PNGs---one
for each axial slice of the data.  You can assume that the third dimension of
the voxel array is the axial dimension.

## Part II - Create a Slice Viewer Page

Now create a new Django view and template that displays the set of PNGs you generated.

Ensure that only one PNG is displayed at a time, and include a slider that
allows the user to quickly slide through the stack of images.

## Other Details

As you code, create logical commits with good commit messages.

If you have any questions about the requirements, ask!  Part of being a good engineer is knowing when to clarify requirements.
