if [ -d "/opt/nvm" ]; then
	export NVM_DIR="/opt/nvm"
	[ -s "/opt/nvm/nvm.sh" ] && . "/opt/nvm/nvm.sh"  # This loads nvm
fi
