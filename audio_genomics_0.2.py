#audio_genomics_0.2.py
#author:beejal
#updated:012617
'''
programs takes an ncbi accession number and converts each
nucleotide to an audible frequency. the entire sequence is saved 
to a sound.wav file.
'''


def main():
    intro()

    sequence_location=2
    emailaddress='me@me.com'
    database='nucleotide'
    identification=input('enter NCBI accession number (enter ab045982 to test a short sequence):')
    #identification='AB045982'
    type='fasta'
    mode='text'

    seq_record=retrieve_sequence(sequence_location,emailaddress,database,identification,type,mode)
    nucleotide2audio(seq_record.seq)

    outro()
    return()


#function intro() prints an introduction onto the console
def intro():
    print('\n\n')
    print('**********\n')
    print('audio genomics version 0.1\n')
    print('tested with python version: 3.6\n')
    print('tested with biopython version: 1.68\n')
    print('**********\n')
    print('\n\n')
    return


'''
function 'retrieve_sequence' uploads a sequence file or connects to
ncbi servers and retrieves a record/sequence for a specific
identification number
function returns 'seq_record'
parameters:
    *sequence_location: 1 to upload a sequence file; 2 to download a
        sequence from ncbi
    *emailaddress: tell ncbi who you are (something@something.com)
    *database: nucleotide; protein; ?
    *identification: identification number
    *type: gb(genbank); fasta; ?
    *mode: text; ?
the arguments rettype="gb" and retmode="text" let us download a record
in the GenBank format
'''
def retrieve_sequence(sequence_location,emailaddress,database,identification,type,mode):
    import sys
    from Bio import Entrez
    from Bio import SeqIO
    if sequence_location==1:
        print('you have chosen to upload a sequence file\n')
        #this section needs to completed
    elif sequence_location==2:
        print('downloading sequence from ncbi...\n')
        try:
            Entrez.email=emailaddress
            handle = Entrez.efetch(db=database, id=identification, rettype=type, retmode=mode)
            seq_record = SeqIO.read(handle, type)
            handle.close()
            #print(seq_record)
            #print(seq_record.id)
            #print(seq_record.name)
            print(seq_record.description)
            print(repr(seq_record.seq))
            print('\n')
            print("sequence length: %i" % len(seq_record))
            return(seq_record)
        except:
            print('unable to download sequence file, check accession number.')
            sys.exit(0)
    return


#converts nucleotide sequence to audio wave file
def nucleotide2audio(sequence):
    import wave, struct, math, time, sys

    sampleRate = 500    # hertz (44100)
    duration = 0.5      # seconds
    #frequency = 200.0  # hertz
    frequency_A = 300.0 # hertz
    frequency_G = 350.0 # hertz
    frequency_C = 400.0 # hertz
    frequency_T = 450.0 # hertz
    print('sample rate (hertz):', sampleRate)
    print('duration (seconds):', duration)
    print('nucleotide A frequency (hertz):', frequency_A)
    print('nucleotide G frequency (hertz):', frequency_G)
    print('nucleotide C frequency (hertz):', frequency_C)
    print('nucleotide T frequency (hertz):', frequency_T)
    counter=1
    wavef = wave.open('sound.wav','w')
    wavef.setnchannels(1) # 1:mono, 2:stereo
    wavef.setsampwidth(2)
    wavef.setframerate(sampleRate)

    for nucleotide in sequence:
        #progress bar
        sys.stdout.write("\rconverting to audio: {}/{}".format(counter, len(sequence)))
        sys.stdout.flush()
        counter+=1

        if nucleotide is 'A':
            for i in range(int(duration * sampleRate)):
                value = int(32767.0*math.cos(frequency_A*math.pi*float(i)/float(sampleRate)))
                data = struct.pack('<h', value)
                wavef.writeframesraw(data)

        elif nucleotide is 'G':
            for i in range(int(duration * sampleRate)):
                value = int(32767.0*math.cos(frequency_G*math.pi*float(i)/float(sampleRate)))
                data = struct.pack('<h', value)
                wavef.writeframesraw(data)

        elif nucleotide is 'C':
            for i in range(int(duration * sampleRate)):
                value = int(32767.0*math.cos(frequency_C*math.pi*float(i)/float(sampleRate)))
                data = struct.pack('<h', value)
                wavef.writeframesraw(data)

        elif nucleotide is 'T':
            for i in range(int(duration * sampleRate)):
                value = int(32767.0*math.cos(frequency_T*math.pi*float(i)/float(sampleRate)))
                data = struct.pack('<h', value)
                wavef.writeframesraw(data)

    wavef.writeframes(b'')
    wavef.close()
    print('\nsound.wav file created and saved')
    return


def outro():
    print('\n\n')
    print('**********\n')
    print('program complete\n')
    print('**********\n')
    print('\n\n')
    return


if __name__ == '__main__':
    main()
