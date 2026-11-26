import importlib.machinery
import importlib.util
import unittest
from pathlib import Path

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


ROOT = Path(__file__).resolve().parents[1]
loader = importlib.machinery.SourceFileLoader("loq_vantage", str(ROOT / "loq-vantage"))
spec = importlib.util.spec_from_loader(loader.name, loader)
app = importlib.util.module_from_spec(spec)
loader.exec_module(app)


class ApplicationTests(unittest.TestCase):
    def test_tray_actions_and_preview_application_id(self):
        preview = app.LOQVantageApp(preview_mode=True)
        normal = app.LOQVantageApp()

        self.assertEqual(preview.get_application_id(), f"{app.APP_ID}.Preview")
        self.assertEqual(normal.get_application_id(), app.APP_ID)
        self.assertIsNotNone(normal.lookup_action("toggle-window"))
        self.assertIsNotNone(normal.lookup_action("quit"))

    def test_user_service_starts_hidden_with_graphical_session(self):
        service = (ROOT / "loq-vantage.service").read_text(encoding="utf-8")

        self.assertIn("ExecStart=/usr/bin/loq-vantage --background", service)
        self.assertIn("WantedBy=graphical-session.target", service)

    def test_rgb_packet_encodes_all_four_zones(self):
        colors = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]

        packet = app.build_rgb_packet(0x01, 2, 1, colors)

        self.assertEqual(len(packet), 33)
        self.assertEqual(packet[:5], bytes([0xCC, 0x16, 0x01, 2, 1]))
        self.assertEqual(packet[5:17], bytes(range(1, 13)))

    def test_wave_packet_sets_only_selected_direction(self):
        colors = [(0, 0, 0)] * 4

        left_to_right = app.build_rgb_packet(0x04, 1, 1, colors, wave_dir=0)
        right_to_left = app.build_rgb_packet(0x04, 1, 1, colors, wave_dir=1)

        self.assertEqual(left_to_right[18:20], bytes([0, 1]))
        self.assertEqual(right_to_left[18:20], bytes([1, 0]))

    def test_application_stylesheet_parses(self):
        provider = Gtk.CssProvider()
        errors = []
        provider.connect(
            "parsing-error",
            lambda _provider, section, error: errors.append(
                f"line {section.get_start_line()}: {error}"
            ),
        )

        provider.load_from_string(app.APP_CSS)

        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
