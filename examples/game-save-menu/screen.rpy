# Anonymous Ren'Py screen-language example.
# Slot content remains runtime-rendered and save compatibility is preserved.

screen archive_save():
    tag menu

    add Solid("#171916")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1540
        ysize 850
        padding (72, 58)
        background Solid("#e8dfca")

        vbox:
            spacing 32

            hbox:
                xfill True
                text "ARCHIVE / SAVE" size 42 color "#29251f"
                null width 40
                text "Runtime slots · synthetic example" size 22 color "#6c6254" yalign 0.5

            grid 3 2:
                spacing 22

                for slot in range(1, 7):
                    button:
                        xsize 440
                        ysize 250
                        action FileSave(slot)
                        has vbox
                        spacing 12

                        add FileScreenshot(slot) xsize 400 ysize 150
                        text FileTime(slot, format=_("%Y-%m-%d  %H:%M"), empty=_("EMPTY SLOT"))
                        key "save_delete" action FileDelete(slot)

            hbox:
                xfill True
                spacing 18
                textbutton _("Previous") action FilePagePrevious()
                textbutton _("Auto") action FilePage("auto")
                textbutton _("Quick") action FilePage("quick")
                textbutton _("Next") action FilePageNext()
                null width 40
                textbutton _("Return") action Return()
