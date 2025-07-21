#!/usr/bin/env python3

import TGHRip.modules.args as args
import TGHRip.modules.assets as assets
import TGHRip.modules.downloader as downloader
import TGHRip.modules.decryptor as decryptor


# === Ctrl+C === #
assets.ctrl_c()


# === MAIN === #
def main():
    """
    Main program flow.
    """
    
    # Banner
    assets.banner(); assets.divider()
    # Arguments
    args.init_args()
    # Hide cursor
    assets.cursor_hide()
    
    # Checking for DRM protections
    encrypted = downloader.is_encrypted(args.url())
    if not encrypted:
        # Download content
        downloader.get_content(args.url())
    else:
        # Download encrypted content
        downloader.get_enc_content(args.url())
        # Extract KID, PR_PSSH, WV_PSSH, KEY
        video_keys, audio_keys = decryptor.extract_keys(args.url())
        # Decrypt content
        decryptor.decrypt(video_keys, audio_keys)
    
    # Merge video & audio files
    if downloader.merge(args.output()):
        # Delete cache files if merged correctly
        downloader.delete_cache()
    
    # Show cursor
    assets.cursor_show()


if __name__ == "__main__":
    main()
