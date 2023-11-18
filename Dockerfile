#
##########################################################################
#       date > log-git-fedora-build.txt; \
#       docker build --no-cache -t fedora . \
#               2>&1 | tee -a log-git-fedora-build.txt; \
#       date >> log-git-fedora-build.txt
############
#
FROM fedora:latest
# Create 'vi' backup and swap directory.
RUN mkdir /root/vim-TMP
RUN dnf upgrade --refresh -y
RUN uname -a
RUN dnf install -y git python3-pip
RUN git --version; python3 --version
# In the 'git-fedora' image 'pip' may be used instead of 'pip3'.
RUN pip install boto3 botocore flake8 pytest requests
RUN pip show pip boto3 botocore flake8 pytest requests 2>&1 | tee /git-fedora-Pip3Boto3versions.txt
# Install a 'vi' configuration file that understands python and yaml syntax.
# File 'virc' is a copy of a useful '.vimrc' file with backup and swap
# directories configured as '/root/vim-TMP'.
# 'mv' should work,
# but making a backup before overwriting is a more conservative approach.
RUN cp -avp /etc/virc /etc/virc_ORG
RUN rm -f /etc/virc
COPY virc /etc/virc
RUN ls -lt /etc/virc*
# FYI 'vim-minmal' provides NO syntax highlighting
# 'syntax on' command will  provoke the following error:
# E319: Sorry, the command is not available in this version
RUN cat /etc/virc
COPY pyfuncs.py test_pyfuncs.py Dockerfile /
RUN pytest /test_pyfuncs.py -vrP 2>&1 | tee /git-fedora-Pytest-results.txt
RUN ls -lrt
ENV MSG='"Hello World from Fedora"'
CMD /bin/echo $MSG
# EOF
