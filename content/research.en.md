# Research

I am interested in phenomena of systems composed of non-equilibrium elements. One example is active matter, which consume energy and turns it into propulsion. Another example is granular particles, whose particle sizes are large enough and thus thermal relaxation is negligible.
Currently, I conduct experiments with bacteria and colloidal systems to measure the magnetic response of active matter.
<img class="research-hero-image" src="/images/research.png" alt="Research image">

## By-products of my study

I designed and built experimental setups to apply magnetic fields to active systems and observe their behavior. Through my projects, I developed skills in the following areas.

### Coil Design and Fabrication

I designed and built coils to apply magnetic fields to samples for microscopic observation. In practice, this requires balancing trade-offs: air-core coils are used to produce a uniform field, while strong fields are also needed. Simply increasing coil turns or current can exceed power-supply limits or overheat and damage the coil.
To address this, I designed coils that can generate sufficiently strong fields within power-supply specifications, while taking the heat generation into account.

### Camera & Coil Controlling Systems

My research requires applying magnetic fields to samples while simultaneously observing samples and monitoring magnetic-field output. To do so, I made applications to control a USB camera (GenICam) and high-speed imaging cameras (FASTCAM). These are operated in synchronization with the coil-related devices described below.
The former (with a USB camera) was implemented in Python, and the latter (with FASTCAM) in C++. Then, devices (coil power supplies and data loggers that monitor coil output) are controlled via SCPI and VISA communication. I also implemented parallel control with the cameras so each device can run concurrently. (This is actually a bit tricky due to VISA-related constraints.)

### CAD Data

I designed each part using CAD to prevent interference between the microscope body and coils, etc. I also created other laboratory accessories (such as tube racks and coil winders).

<div class="research-gallery" role="region" aria-label="Coil design gallery">
	<div class="research-gallery-track" tabindex="0">
		<section class="research-gallery-slide" id="coil-pair-1" aria-label="Pair 1 of 3">
			<img src="/images/pic1_coilreelcad.jpg" alt="CAD model of coil reel" loading="lazy">
			<img src="/images/pic1_coilreelpic.jpg" alt="Fabricated coil reel" loading="lazy">
			<div class="research-gallery-controls">
				<a class="research-gallery-btn" href="#coil-pair-3" aria-label="Show previous pair">&#9664;</a>
				<a class="research-gallery-btn" href="#coil-pair-2" aria-label="Show next pair">&#9654;</a>
			</div>
		</section>
		<section class="research-gallery-slide" id="coil-pair-2" aria-label="Pair 2 of 3">
			<img src="/images/pic2_coilcad.jpg" alt="CAD model of coil setup" loading="lazy">
			<img src="/images/pic2_coilpic.jpg" alt="Assembled coil setup" loading="lazy">
			<div class="research-gallery-controls">
				<a class="research-gallery-btn" href="#coil-pair-1" aria-label="Show previous pair">&#9664;</a>
				<a class="research-gallery-btn" href="#coil-pair-3" aria-label="Show next pair">&#9654;</a>
			</div>
		</section>
		<section class="research-gallery-slide" id="coil-pair-3" aria-label="Pair 3 of 3">
			<img src="/images/pic3_coilcad.jpg" alt="CAD model of microscope coil component" loading="lazy">
			<img src="/images/pic3_coilpic.jpg" alt="Fabricated microscope coil component" loading="lazy">
			<div class="research-gallery-controls">
				<a class="research-gallery-btn" href="#coil-pair-2" aria-label="Show previous pair">&#9664;</a>
				<a class="research-gallery-btn" href="#coil-pair-1" aria-label="Show next pair">&#9654;</a>
			</div>
		</section>
	</div>
</div>