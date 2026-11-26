#!/usr/bin/env bash
set -euo pipefail

echo "=== Menghapus instalasi LOQ Vantage ==="

FILES=(
    "/usr/bin/loq-vantage-ctl"
    "/usr/bin/loq-vantage"
    "/usr/share/polkit-1/actions/com.lenovo.loqvantage.policy"
    "/etc/polkit-1/rules.d/49-loq-vantage.rules"
    "/usr/lib/udev/rules.d/99-loq-vantage.rules"
    "/usr/share/applications/loq-vantage.desktop"
)

for file in "${FILES[@]}"; do
    if [[ -e "$file" ]]; then
        sudo rm -f "$file"
        echo "-> Dihapus: $file"
    fi
done

# Muat ulang aturan udev
sudo udevadm control --reload-rules
sudo udevadm trigger --subsystem-match=hidraw

# Perbarui cache menu aplikasi jika tersedia
if command -v update-desktop-database >/dev/null 2>&1; then
    sudo update-desktop-database /usr/share/applications || true
fi

echo "=== LOQ Vantage berhasil dihapus dari sistem. ==="
echo "Catatan: Folder sumber di $(pwd) tidak dihapus otomatis."