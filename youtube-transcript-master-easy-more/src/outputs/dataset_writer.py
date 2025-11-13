thonimport os
import json
import logging

def write_to_output(data, output_dir):
    logging.info(f"Writing data to {output_dir}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_file = os.path.join(output_dir, 'transcript_output.json')
    with open(output_file, 'w') as f:
        f.write(data)