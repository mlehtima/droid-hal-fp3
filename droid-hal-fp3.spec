# These and other macros are documented in dhd/droid-hal-device.inc
%define device FP3
%define vendor fairphone

%define rpm_device fp3
%define rpm_vendor fairphone

%define droid_target_aarch64 1

%define have_custom_img_boot 1
%define have_custom_img_recovery 1

%define enable_dtbo_update 1

#define installable_zip 1
#define enable_kernel_update 1

# want adreno quirks is required for browser at least, and other subtle issues
%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

%define makefstab_skip_entries /dev/stune /dev/cpuset /sys/fs/pstore /sys/fs/bpf /dev/cpuctl /dev/mtp

%define straggler_files \
/bugreports\
/cache\
/d\
/product\
/product_services\
/sdcard\
%{nil}

%define additional_post_scripts \
/usr/bin/groupadd-user media_rw || :\
%{nil}

%include rpm/dhd/droid-hal-device.inc
