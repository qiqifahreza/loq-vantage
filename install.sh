#!/usr/bin/env bash
set -euo pipefail

echo "=== Menginstal LOQ Vantage untuk Arch Linux ==="
sudo install -Dm755 loq-vantage-ctl /usr/bin/loq-vantage-ctl
sudo install -Dm755 loq-vantage /usr/bin/loq-vantage
sudo install -Dm644 com.lenovo.loqvantage.policy /usr/share/polkit-1/actions/com.lenovo.loqvantage.policy
sudo install -Dm644 99-loq-vantage.rules /usr/lib/udev/rules.d/99-loq-vantage.rules
sudo install -Dm644 loq-vantage.desktop /usr/share/applications/loq-vantage.desktop

read -rp "Izinkan user grup 'wheel' mengubah pengaturan tanpa popup password Polkit? [y/N]: " ans
if [[ "${ans,,}" == "y" ]]; then
    sudo install -Dm644 49-loq-vantage.rules /etc/polkit-1/rules.d/49-loq-vantage.rules
    echo "-> Polkit passwordless rule dipasang."
fi

sudo udevadm control --reload-rules
sudo udevadm trigger --subsystem-match=hidraw

echo "=== Selesai! Jalankan 'loq-vantage' dari terminal atau menu aplikasi. ==="