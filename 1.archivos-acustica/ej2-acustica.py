#!/usr/bin/python
# -*- coding: latin-1 -*-

import numpy as np
import pylab
import matplotlib.pyplot as pyplot
import scipy.io.wavfile


def ondasimple(t, f, p=0):
  return np.sin(2 * np.pi * f * t + p)


def plot(mionda, name):
    # Graficamos la onda.
    pyplot.clf()
    pyplot.plot(ts[0:500], mionda[0:500])
    pyplot.savefig('{}.png'.format(name))


    # La guardamos como wav.
    wavdata = np.array(mionda * 10000.0, dtype=np.int16)
    scipy.io.wavfile.write('{}.wav'.format(name), 16000, wavdata)


    # Mostramos su espectrograma.

    pyplot.clf()
    sgram = pylab.specgram(mionda, Fs=16000.0)
    pyplot.colorbar()
    pyplot.savefig('{}_espectrograma.png'.format(name))



# Generamos 16000 puntos a 16kHz.
ts = np.arange(16000.0) / 16000.0


def main():
    # Armamos una onda senoidal discretizada con f=1000Hz.
    mionda1 = ondasimple(ts, 1000)

    # Armamos una onda senoidal discretizada con f=100Hz.
    mionda2 = ondasimple(ts, 100)

    # Combinamos ambas ondas periódicas simples, para
    # formar una onda periódica compuesta.
    mionda = mionda1 + mionda2

    plot(mionda, 'mionda')


# Ejercicios:
#
# 1. Crear una onda de ruido blanco y mostrar su espectrograma.
#    Ayuda: Usar 'random.uniform(-1, 1)' del módulo random.
#
# 2. Crear una senoidal simple y combinarla con ruido blanco. Mostrar su
#    espectrograma.
#
# 3. Crear una senoidal simple con frecuencia ascendente y mostrar su
#    espectrograma.
#
# 4. Combinar dos senoidales con frecuencias 1000 y 100Hz con distintas
#    fases (ej: 0 y pi), y comparar las formas de onda. ¿Tiene algún efecto
#    perceptual el cambio de fase?
# 
# 5. Crear dos senoidales simples con la misma frecuencia pero distintas
#    fases, de modo que al combinarlas se anulen.
#    http://en.wikipedia.org/wiki/Active_noise_control

def ej1():
    noise = np.random.RandomState(42).uniform(low=-1, high=1, size=len(ts))
    plot(noise, 'noise')

def ej2():
    noise = np.random.RandomState(42).uniform(low=-1, high=1, size=len(ts))
    mionda = ondasimple(ts, 100)
    dirty = noise + mionda
    plot(dirty, 'dirty')

def ej3():
    asc = np.sin(2 * np.pi * ts * (ts * 16000 * 0.25) )
    plot(asc, 'asc')

def ej4():
    a = ondasimple(ts, 100)
    b_no_phase = ondasimple(ts, 1000)
    b_phase = ondasimple(ts, 1000, np.pi)
    plot(a + b_no_phase, 'abnophase')
    plot(a + b_phase, 'abphase')

def ej5():
    a = ondasimple(ts, 100)
    ap = ondasimple(ts, 100, np.pi)
    plot(a + ap, 'cancel')

if __name__ == '__main__':
    ej5()