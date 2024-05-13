import tensorflow as tf
from discriminator import build_discriminator
from generator import build_generator
import numpy as np

def load_real_data(filename):
    with open(filename, 'r') as infile:
        return[float(line.strip()) for line in infile]
    

def generate_fake_samples(generator, n_samples):
    # Generate random noise
    noise = np.random.normal(0, 1, (n_samples, 10))
    # Generate fake data
    return generator.predict(noise)


def train_gan(generator, discriminator, gan_model, real_data, epochs=1000, batch_size=128, visualize=False):
    half_batch = batch_size//2

    for epoch in range(epochs):
        # Train discriminator
        # Select a random half batch for real data
        idx = np.random.randint(0, len(real_data), half_batch)
        real_samples = real_data[idx] 

        # Generate a half batch of fake data
        fake_samples = generate_fake_samples(generator, half_batch)

        real_labels = np.ones((half_batch,1))
        fake_labels = np.zeros((half_batch, 1))



def create_gan_model(alpha=2.0, descriminator_lr=0.0001, generator_lr=0.0001, epochs=1000, save_model=False, model_path='./Maj/8 Maj/models/gan_models.keras'):
    discriminator = build_discriminator()
    generator = build_generator()

    # Build combined GAN model 
    initial_noise = tf.keras.Input(shape=(10,))
    initial_fake = generator(initial_noise)
    discriminator.trainable = False
    validity = discriminator(initial_fake)
    gan_model = tf.keras.Model(initial_noise, validity)

    gan_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    real_data = load_real_data('./Maj/8 Maj/data/random_numbers.txt')

    # Train GAN 
    train_gan(generator, discriminator, gan_model, real_data, epochs=epochs, visualize=False)




create_gan_model