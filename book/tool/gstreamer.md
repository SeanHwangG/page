# Gstreamer

## Overview

![alt](.gitbook/assets/20210207_231800.png)

* framework for creating multitype streaming media application for video, audio
* used to build media player supporting a variety of formats
* [+] pluggable components can be mixed into arbitrary pipelines, full-fledged video or audio editing app

```text
protocol handling   # file, http, rtsp
sources             # alsa, v4l2
formats             # avi, mp4, ogg
codecs              # mp3, mpeg4, vorbis
filters             # converters, mixers, effects
sinks               # alsa, xvideo, tcp / udp
```

### Setup

> Install

* ubuntu

```text
sudo apt-get install gtk+-3.0 
sudo apt-get install libgstreamer-plugins-base1.0
```

* mac
* sudo brew

```text
sudo brew install gtk+-3.0
```

> Run

```text
gcc file_name.c -o file_name `pkg-config --cflags --libs gstreamer-video-1.0 gtk+-3.0 gstreamer-1.0`
```

### Term

> pad

* elements input and output, where you can connect other elements
* viewed as plug or port on the element (restrict the type of data)

> bin

* container for a collection of elements, mostly control a bin as if it were an element

> pipeline

* a top-level bin provides a bus for application and manages synchronization for its children

> communication

![alt](.gitbook/assets/20210207_232135.png)

```text
buffer        # objects for passing streaming data between elements 
events        # objects sent between elements which can travel upstream / downstream
messages      # objects posted by elements on pipeline’s message bus
query         # allow application to request information
```

### Plugin

```text
gst-plugins-base    # exemplary set of elements
gst-plugins-good    # set of good-quality plug-ins under LGPL
gst-plugins-ugly    # set of good-quality plug-ins that might pose distribution problems
gst-plugins-bad     # set of plug-ins that need more quality
gst-libav           # set of plug-ins that wrap libav for decoding and encoding
```

## Command

> gst-inspect-1.0

```text
plugin_name         # inspect plugin_name
```

> gst-launch-1.0

```text
-e, --eos-on-shutdown     # Force EOS on sources before shutting the pipeline down

export GST_DEBUG=gvatracker:5    # enable log
```

### Src

* do not accept data, only generate data (reading from disk or from a sound card)

> videotestsrc

```text
pattern             # smpte (0) / snow (1) / colors (24) – Colors
framerate=1/5
```

> filesrc

```text
Read data from a file in the local file system
```

> multifilesrc

* Reads buffers from sequentially named files
* to use with an image decoder, use “caps” property or a capsfilter to force to caps containing a framerate

### Filter

> GstPad queue(GstPad)

* specified by GstQueue:max-size-buffers, GstQueue:max-size-bytes GstQueue:max-size-time properties
* Any attempt to push more buffers into queue will block pushing thread until more space becomes available

> h264parse

* Parses H.264 streams

> timeoverlay

* overlays the buffer timestamps of a video stream on top of itself

> pngdec

* Decodes png images. If there is no framerate set on sink caps, it sends EOS after the first picture

```text
# src
video/x-raw     # format (RGBA, RGB, ARGB64, GRAY8, GRAY16_BE), width,height / framerate

# sink
image/png:
```

> vaapi264dec

* decodes from H264 bitstreams to surfaces suitable for vaapisink or vaapipostproc elements 
* use installed VA-API back-end

> videoconvert

* Convert video frames between a great variety of video formats.

> video/x-raw

### Sink

* endpoints in a media pipeline (Disk writing, soundcard playback, and video output)

> fakesink

```text
location=test.avi    # save to video
```

> multifilesink

```text
location=img%d.png
max-files           # Max files to keep on disk. old files start to be deleted to make room for new ones
```

### Error

> No such element or plugin 'gvatracker'

```text
gst-inspect-1.0 gvatracker
```

* echo $GST_PLUGIN_PATH

> ERROR: from element /GstPipeline:pipeline0/GstH264Parse:h264parse0: Failed to parse stream

```text
gst-launch-1.0 -e multifilesrc location=/home/root/mot17/train/MOT17-02-SDP/yuv_raws/frame%d.yuv index=1 ! h264parse ! vaapih264dec  !  fakesink sync=false
```

> WARNING: erroneous pipeline: could not link multifilesrc0 to videoconvert0

```text
gst-launch-1.0 -e multifilesrc location="/home/root/mot17/train/MOT17-02-SDP/yuv_raws/frame%d.yuv" caps="image/yuv,framerate=(fraction)12/1" index=1  ! videoconvert ! fakesink sync=false
```

> ERROR: from element /GstPipeline:pipeline0/GstMultiFileSrc:multifilesrc0: Internal data stream error.  
> Additional debug info:  
> ../gstreamer-1.16.0/libs/gst/base/gstbasesrc.c(3072): gst_base_src_loop (): /GstPipeline:pipeline0/GstMultiFileSrc:multifilesrc0:  
> streaming stopped, reason not-negotiated (-4)  
> ERROR: pipeline doesn't want to preroll.

* Wrong multifilesrc location

```text
gst-launch-1.0 -e multifilesrc location=frame%d.yuv index=1  ! gvatracker profile=true !  fakesink sync=false
```

## C++

* [https://gstreamer.freedesktop.org/documentation/tutorials/basic/hello-world.html?gi-language=c](https://gstreamer.freedesktop.org/documentation/tutorials/basic/hello-world.html?gi-language=c)

### GstBus

```text
GObject
    ╰──GInitiallyUnowned
        ╰──GstObject
            ╰──GstBus
```

* object responsible for delivering GstMessage packets in a first-in first-out way from streaming threads to the application
* marshall the messages between different threads

> GstMessage _gst_bus_timed_pop_filtered(GstBus_ bus,  
> GstClockTime timeout,  
> GstMessageType types)

* Get a message from a bus whose type matches message type mask types, waiting up to the specified timeout
* discarding any messages that do not match the mask provided
* with timeout 0, behaves like gst_bus_pop_filtered. 
* with timeout GST_CLOCK_TIME_NONE, block until a matching message was posted on the bus

### GstMap

> gst_buffer_map(buffer)

### GstBin

![alt](.gitbook/assets/20210208_012758.png)

> gst_bin_get_by_name (GstBin _bin, const gchar_ name)

* Gets the element with the given name from a bin recursing into child bins.
* Returns NULL if no element with the given name is found in the bin.
* MT safe. Caller owns returned reference.

> gst_bin_add_many (GST_BIN (pipeline), source, filter, sink, NULL);
>
> gst_object_unref(gst_element)
>
> g_warning ("Failed to link elements!");

### GstBuffer

* Basic unit of data transfer in GStreamer
* contain timing and offset along with other arbitrary metadata that is associated with GstMemory blocks that buffer contains

> GstBuffer * gst_buffer_new()

* Creates a newly allocated buffer without any data.

> gstbuffer_make_writable(GstBuffer buffer)

* Returns a writable copy of buf, if source buffer is already writable, this will simply return the same buffer

### GstElement

* abstract base class needed to construct an element that can be used in a GStreamer pipeline
* contains GList of GstPad structures for all their input (sink) and output (source) pads

* GST_STATE_NULL (default)
  * No resources are allocated in this state, so, transitioning to it will free all resources. 
  * The element must be in this state when its refcount reaches 0 and it is freed.

* GST_STATE_READY
  * an element has allocated all of its global resources, that is, resources that can be kept within streams
  * You can think about opening devices, allocating buffers and so on 
  * However, the stream is not opened in this state, so the stream positions is automatically zero If a stream was previously opened, it should be closed in this state, and position, properties and such should be reset.

* GST_STATE_PAUSED
  * an element has opened the stream, but is not actively processing it.
  * An element is allowed to modify a stream's position, read and process data and such to prepare for playback as soon as state is changed to PLAYING 
  * it is not allowed to play the data which would make the clock run
  * PAUSED is the same as PLAYING but without a running clock.
  * Elements going into the PAUSED state should prepare themselves for moving over to the PLAYING state as soon as possible. 
  * Video or audio outputs would, for example, wait for data to arrive and queue it so they can play it right after the state change. 
  * Also, video sinks can already play the first frame since this does not affect the clock yet). 
  * Autopluggers could use this same state transition to already plug together a pipeline. 
  * Most other elements, such as codecs or filters, do not need to explicitly do anything in this state, however.

* GST_STATE_PLAYING
  * an element does exactly the same as in the PAUSED state, except that the clock now runs.

* GstElement _gst_parse_launch (const gchar_ pipeline_description, GError ** error)
  * gst_element_link_many (source, filter, sink, NULL)
* gst_element_factory_make (factory_name, element_name)
  * name of the element is something you can use later on to look up the element in a bin
* gst_object_unref ()
  * unref, decrease reference count by 1
* gst_element_factory_find(factory, GST_ELEMENT_METADATA_KLASS)
* gst_element_factory_get_metadata()
* gst_element_get_name() / gst_element_set_name()

> getter and setter

* gst_element_add_pad() / gst_element_remove_pad()
* gst_element_iterate_pads()
* gst_element_set_state ()
* gst_element_sync_state_with_parent ()

### GstPipeline

![alt](images/20210208_012953.png)

* chain of elements create pipeline, links are allowed when two pads are compatibles
* element has one specific function (reading data from file, decoding data)

* gst_pipeline_new ("my-pipeline");
  * create new pipeline

### GstPad

```text
GObject
    ╰──GInitiallyUnowned
        ╰──GstObject
            ╰──GstPad
                ╰──GstProxyPad
```

* GstPad _gst_element_get_static_pad (GstElement_ element, const gchar * name);
  * Retrieves a pad from element by name
  * This version only retrieves already-existing (i.e. 'static') pads.

* gst_pad_get_parent()
  * retrieve GstElement that owns the pad

* GstParse()

```cpp
#define GST_PARSE_ERROR gst_parse_error_quark ()   // get an error quark of parse subsystem
#define GST_TYPE_PARSE_CONTEXT (gst_parse_context_get_type())
```

### GstProbe

* callback that can be attached to a pad
* run in the pipeline's streaming thread context
  * one should usually avoid calling GUI-related functions from within a probe callback
  * nor try to change the state of the pipeline

> Dataprobe

* Data probes notify you when there is data passing on a pad

* GST_PAD_PROBE_TYPE_BUFFER
  * A buffer is pushed or pulled

> gulong gst_pad_add_probe(GstPad * pad,  
> GstPadProbeType mask,  
> GstPadProbeCallback callback,  
> gpointer user_data,  
> GDestroyNotify destroy_data)

* Be notified of different states of pads. callback is called for every state that matches mask

* gst_pad_remove_probe()
  * remove callback
