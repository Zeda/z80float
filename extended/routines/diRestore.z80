#ifndef included_diRestore
#define included_diRestore
diRestore:
;Adds 151cc if interrupts are enabled, 161cc if disabled
;Disables interrupts, but sets up the stack so that interrupt settings are restored.
;Call this at the top of your routine that needs to disable interrupts :)
  ex (sp),hl
  push hl
  push af
  ld hl,restoreei
  ld a,r
  jp pe,+_
  ld hl,restoredi
_:
  di
  pop af
  inc sp
  inc sp
  ex (sp),hl
  dec sp
  dec sp
  ret
restoredi:
  di
  ret
restoreei:
  ei
  ret
#endif
