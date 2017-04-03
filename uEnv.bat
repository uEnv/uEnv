@echo off
PATH=%PATH%;X:\.sys\uenv
PATH=%PATH%;X:\.sys\cubo
PATH=%PATH%;X:\Software
PATH=%PATH%;X:\abc
start "uEnv BETA_20170403-1" cmd.exe /s /k .\.sys\clink-0.4.8\clink_x86.exe inject